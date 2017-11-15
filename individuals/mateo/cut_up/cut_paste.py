import requests
import bs4
import json
import re

import sys
import getopt

# Define filter for new releases tag (different in main page vs browse by tag)
def pnrFilter(id):
    new = (id == "tab_newreleases_content" or id == "tab_PopularNewReleases_content") and bNew
    top = (id == "tab_topsellers_content" or id == "tab_TopSellers_content") and bTop
    return new or top

# Functions to build Steam store links to maximise our scraping fun :)
def steamURL(tag = None, page = 0, tab = None):
    store = "https://store.steampowered.com"

    if tag is not None:
        store += "/tag/en/"
        store += tag
        store += "/#p="
        store += str(page)

    return store

def categoryURL(tagNum, page):
    url = "http://store.steampowered.com/search/?tags="
    url += str(tagNum)
    url += "&page="
    url += str(page)

    return url

# Retrieve command line arguments to scrape by tag
bTag = False
bNew = False
bTop = False
bJson = False
bDone = False

max = 500
output = None
tag = None
tab = None

try:
    opts, args = getopt.getopt(sys.argv[1:], "hj", ["new", "top", "tag=", "max=", "out="])
except getopt.GetoptError:
    print("oop wrong option")
    sys.exit()
for opt, arg in opts:
    if opt == '--new':
        bNew = True
        tab = "PopularNewReleases"
    elif opt == '--top':
        bTop = True
        tab = "TopSellers"
    elif opt == '--tag':
        bTag = True
        tag = str(arg)
    elif opt == '--max':
        max = int(arg)
    elif opt == '--out':
        output = str(arg)
    elif opt == '-h':
        print("""HELPFUL HELP 
        --tag [tag]      : Tag to search 
        --max [number]   : Maximum number of reviews (default is 500) 
        --out [filename] : Where to save the reviews (as .txt)
        -j               : Save as JSON too""")
        sys.exit()
    elif opt == '-j':
        bJson = True

if not (bNew or bTop):
    bNew = True
    bTop = True

if bTag:
    print ("Tag: ", tag)

# Set up object for JSON output
data = {
    "tag" : None,
    "tagId" : None,
    "count": 0,
    "games" : []
    }

# Prepare text file for raw output
if output is None:
    output = "out"

with open(output + ".txt", "w") as file:
    # =============== BASE LEVEL: Scrape Steam Category ===============
    # ==== We should get Tag ID to find a better, non-dynamic list ====

    # Build base URL to scrape: Steam homepage or related tag page (if tag is specified)
    store = steamURL(tag)

    # Request our HTML!
    storeReq = requests.get(store)

    print("Scraping ", storeReq.url, " for a better link") #Game IDs and links... Page ", page)

    # JS ALERT: Pagination is dynamic :(
    # But there is another page with more games per list, let's scrape it!

    parsedStore = bs4.BeautifulSoup(storeReq.text, "html.parser")
    betterLink = parsedStore.find(class_ = "btn_small_thin")["href"]

    # Use RegExp to find the Tag ID!
    regex = re.compile(r'\d+') # RegEx matches any sequence of 1 or more digits
    tagID = regex.search(betterLink).group()
    print("Our ID is ", tagID)

    data["tag"] = tag
    data["tagId"] = tagID

    # Now we're ready to roll!
    # Keep track of how many reviews we've got and which page we're scraping
    page = 1
    numGames = 0
    counter = 0
    curLink = ""
    betterReq = None
    parsedBetter = None
    ntLinks = []

    # Prepare game + review data array
    gameData = []
    curGame = {}

    # Start loopin'
    while True:   
        # ============= ONE LEVEL DOWN:  Scrape full Category Page =============
        # ==== This one should be non-dynamic and provide 25 games per page ====

        # Craft our new URL
        curLink = categoryURL(tagID, page)

        # Request the better link
        betterReq = requests.get(curLink)
        print("Scraping Game IDs and links with Tag", tag, " page", page, " :: ", curLink, "\n")

        parsedBetter = bs4.BeautifulSoup(betterReq.text, "html.parser")
        ntLinks = parsedBetter.find_all(class_ = "search_result_row") #find(id = pnrFilter).find_all(class_ = "tab_item")

        # Prepare game item
        curGame = {
            "title" : None,
            "id" : None,
            "reviews" : []
            }

        for link in ntLinks:
            # ==== TWO LEVELS DOWN: Use links/IDs to request game review page ====
            # ===== We should find the review page to start scraping reviews =====

            # Game page link loads reviews via JS so it sucks
            # Steam Community site loads a bunch of reviews by default (no JS!)
            # Gotta extract the game's ID from our original href

            regex = re.compile(r'\d+') # RegEx matches any sequence of 1 or more digits
            id = regex.search(link["href"]).group() # We find our number...

            print("Requesting reviews page for game with ID ", id)

            # Actually request da reviews!
            try:
                gameReq = requests.get("https://steamcommunity.com/app/" + id + "/reviews/?browsefilter=toprated&snr=1_5_reviews_&filterLanguage=english")
                print("Got page with status ", gameReq.status_code)
            except requests.exceptions.TooManyRedirects:
                print("Whoops crazy redirects, skipping!")
                continue

            # Parse game community page to scrape reviews!
            parsedGame = bs4.BeautifulSoup(gameReq.text, "html.parser")

            title = parsedGame.find(class_ = 'apphub_AppName');    
            reviews = parsedGame.find_all(class_ = "apphub_CardTextContent")

            if title is None or reviews is None:
                print("Nothing found!")
                continue

            print("Getting reviews for ", title.text)

            curGame['title'] = title.text
            curGame['id'] = id

            # Prepare reviews array
            reviewData = []

            howMany = 0
            for review in reviews:
                # =========== THREE LEVELS DOWN: Time to grab the reviews ===========
                # ==== We finally got the review page so we just gotta save them ====
                try:
                    nonAlpha = re.compile(r'''(?![.]\w*[.])[.!?]+|\s\s+|[\n\r]''')
                    text = nonAlpha.split(review.text)

                    textList = []

                    for fragment in text:
                        if fragment is not "":
                            file.write(fragment + '\n')

                    for fragment in text:
                        if fragment is not "":
                            textList.append(fragment)

                    reviewData.append(textList)

                    howMany += 1
                    counter += 1
                except UnicodeEncodeError:
                    print("Faulty encoding! Skipping to the next one...")

                if counter >= max:
                    # ==== DONE! ====
                    print("Found", howMany, " reviews!")
                    print("Done scraping", max, "reviews for", numGames + 1, tag,  "games! Yay!")
                    bDone = True
                    break
                    #sys.exit()
            
            # ==== BACK UP ONCE: Count reviews for this game, go to the next ====
            print("Found ", howMany, " reviews!\n")

            curGame["reviews"] = reviewData
            gameData.append(dict(curGame))

            numGames += 1
            if bDone:
                break

        # ==== BACK UP TWICE: Done with the page, time for the next! ====
        page += 1
        if bDone:
            break

    data["games"] = gameData
    data["count"] = counter

    if bJson:
        with open(output + ".json", "w") as jFile:
            print("Writing to JSON...")
            text = json.dumps(data)
            jFile.write(text)

    print("All done! :D")