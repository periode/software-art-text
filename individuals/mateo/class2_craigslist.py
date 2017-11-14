import requests # a module to make HTTP requests!
import bs4 # Beautiful Soup parses and makes our html data pretty and navigatable
import json # yaaay JSON

# ================ REQUEST ========================================
request = requests.get("https://newyork.craigslist.org/search/mis") # GET request

print(request.status_code) # we can access the request's response code to make sure stuff works

# ================= PARSE =========================================
parsed = bs4.BeautifulSoup(request.text, "html.parser") # Beautiful Soup preses our HTML!

results = parsed.find_all("a", class_ = "hdrlnk"); # Now we can filter and find stuff within our HTML

current = ""
currentparsed = 0;
currenttext = ""

with open("daResults.txt", "w") as daFile: # create/open a text file!
    for result in results:
        #print(result.prettify()) # prettify makes stuff more readable
        #print(result["href"]) # we can get attributes from each result

        current = requests.get(result["href"])
        currentparsed = bs4.BeautifulSoup(current.text, "html.parser")
        currenttext = currentparsed.find(id="postingbody").text # prettify()) # text to extract actual text content, prettify for formatted html
        printy = currenttext.replace("QR Code Link to This Post", "").strip()

        print(printy) 

        daFile.write(printy); # write to the file!
