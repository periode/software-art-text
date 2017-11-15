import requests #the requests module to get a URL
from bs4 import BeautifulSoup #the beautiful soup module to make sense of the data
import json #json to save it as json

target_url = "http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html"
offline_url = "file:///Desktop/death_row_information.html"
everyone = [] #this is the array where we will store all the information

#in python, we need to define our functions BEFORE calling them
#this is the function for saving data to disk
def save(data):
    
    #this is how we open a file to either read ('r') or write ('w')
    #if the file doesn't exist, it will be created.
    #if the file exists, it will be overwritten
    with open("everyone.json", 'w') as open_file:

        #json.dumps transforms any data we have into a data object
        json.dump({'executed' : data}, open_file)

#this is the function where we go through the webpge and extract what we want
def parse(content, everyone):

    #first, we turn everything into a readable format
    soup = BeautifulSoup(content, "html.parser")

    #then we want all the <tr> tags
    all_deceased = soup.find_all("tr")

    #then all the <a> tags
    links = soup.find_all("a")

    #now we go through all the lines in the table
    for deceased in all_deceased:
        
        first = deceased.contents[9].string.strip() #we get the first name (9th element in the row)
        last = deceased.contents[7].string.strip() #and the last name (7th element)
        
        #now we go through all the links to find out if they match the name
        for link in links:
            if str(first).lower() in str(link['href']) and 'last' in str(link['href']): #does it match? and does it have 'last' in it?
                last_statement = str(link['href'])
                break
            else:
                last_statement = "none"

        #now we create a dict (kinda like a JSON object)
        person = {
                'first': first,
                'last': last,
                'link': last_statement,
                'statement': ""
                }
        everyone.append(person)

    save(everyone) #and now we save everything!


#THIS IS THE ACTUAL BEGINNING OF THE PROGRAM
req = requests.get(target_url)
print "getting url: %s" % target_url
if req.status_code == 200: #can we get it online?
    print "got result!"
    parse(req.text, everyone)
else: #if not we get it offline
    print "something went wrong, response code %i" % req.status_code
    print "opening offline version"
    with open("death_row_information.html", 'r') as raw:
        parse(raw, everyone)
