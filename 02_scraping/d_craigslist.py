import requests                                                                             #this we need for getting the page
import bs4                                                                                  #this we need for making sense of the html page
import json                                                                                 #this we need to save our data as JSON

all_postings = []                                                                           #here we will temporarily store all the postings we find
currently_scraping_count = 0                                                                #we keep track of which posting we're currently scraping

#################################### THIS IS THE REQUEST PART
url_to_scrape = "https://newyork.craigslist.org/search/mis"
our_request = requests.get(url_to_scrape)                                                   #getting the html page
print "requested page sent response code: %s" % our_request.status_code                     #we should get a 200 response code

#################################### THIS IS THE PARSING PART
parsed_html = bs4.BeautifulSoup(our_request.text, 'html.parser')                            #we load everything inside BeautifulSoup and we tell it to interpret it using HTML

#now we can perform searches and manipulations.
#in our case, looking for all the p tags with the class "hdrlnk"
all_results = parsed_html.find_all(class_="hdrlnk")

#go through all the elements in the list and print them one by one
for result in all_results:
    single_url = result['href']                                                             #we find the URL for each link, since it is the value of the href attribute
    single_request = requests.get(single_url)                                               #we request each individual posting, doing a new GET request
    parsed_posting = bs4.BeautifulSoup(single_request.text, "html.parser")                  #we parse the page again through BS
    posting_body = parsed_posting.find_all(id="postingbody")                                #in that parsed page, we find all the tags with the id "postingbody"
    cleaned_posting = posting_body[0].text.replace("QR Code Link to This Post", "").strip() #we get rid of that text we don't want, and we call strip(), which removes any white space at the beginning or end of the string
    currently_scraping_count += 1                                                           #we increase the count by one, since we've scraped one more url
    print "scraped posting: %i/%i" % (currently_scraping_count, len(all_results))           #we use the variable on the line above to print the progress
    properly_encoded_posting = cleaned_posting.encode('utf-8')                              #even though it might be clean, it might not be properly encoded, so we make sure it's unicode (i.e. utf-8) compliant
    all_postings.append(properly_encoded_posting)                                           #finally, we add it to our list (i.e. our array)


print "done scraping! writing to file..."

#################################### THIS IS THE WRITING PART
with open("all_results.json", 'w') as my_file:                                              #this is how you open a file. the 'w' means we are going to write to it.
    data_to_write = json.dumps(all_postings)                                                #because we have an array, we need to turn it into a string before writing
    my_file.write(data_to_write)                                                            #and finally we write!
