import requests                                                                             #this we need for getting the page
import bs4                                                                                  #this we need for making sense of the html page
import json                                                                                 #this we need to save our data as JSON

all_postings = []                                                                           #here we will temporarily store all the postings we find
currently_scraping_count = 0                                                                #we keep track of which posting we're currently scraping

#open file with all urls 
#################################### THIS IS THE REQUEST PART
url_to_scrape = "https://www.tripadvisor.com/Attractions-g60827-Activities-Brooklyn_New_York.html"
our_request = requests.get(url_to_scrape)                                                   #getting the html page
print "requested page sent response code: %s" % our_request.status_code                     #we should get a 200 response code

#################################### THIS IS THE PARSING PART
parsed_html = bs4.BeautifulSoup(our_request.text, 'html.parser')                            #we load everything inside BeautifulSoup and we tell it to interpret it using HTML

#now we can perform searches and manipulations.
#in our case, looking for all the p tags with the class "hdrlnk"
all_results = parsed_html.find_all(class_="poiTitle")

j=0
i=2
#go through all the elements in the list and print them one by one
for result in all_results:
    j+=1
    single_url = result['href']                                                             #we find the URL for each link, since it is the value of the href attribute
    single_url1="https://www.tripadvisor.com"+single_url

    a=str(single_url1)
    i=1
    for i in range(1,7):
        print i
        b=i*10
        c=str(b)
        single_url2=a[:69]+"or"+c+"-"+a[69:]
        single_request = requests.get(single_url2)                                               #we request each individual posting, doing a new GET request
        #print single_url2
        parsed_posting = bs4.BeautifulSoup(single_request.text, "html.parser")                  #we parse the page again through BS
        all_results1=parsed_posting.find_all(class_="quote")
        i+=1
        
   
        for result in all_results1:
            results2=result.find_all('a', href=True, text=True)
            for result in results2:
                single_url3=result['href']                                                           #we find the URL for each link, since it is the value of the href attribute
                single_url4="https://www.tripadvisor.com"+single_url3
                single_request2 = requests.get(single_url4)
            #print single_url4
                parsed_posting1 = bs4.BeautifulSoup(single_request2.text, "html.parser")
        
                posting_body = parsed_posting1.find_all(class_="partial_entry")                                #in that parsed page, we find all the tags with the id "postingbody"
    
                cleaned_posting = posting_body[0].text.replace("QR Code Link to This Post", "").strip() #we get rid of that text we don't want, and we call strip(), which removes any white space at the beginning or end of the string
                currently_scraping_count += 1                                                           #we increase the count by one, since we've scraped one more url
                properly_encoded_posting0 = cleaned_posting.encode('utf-8')                              #even though it might be clean, it might not be properly encoded, so we make sure it's unicode (i.e. utf-8) compliant
                properly_encoded_posting=properly_encoded_posting0.split(".") 
                all_postings.append(properly_encoded_posting)
                print properly_encoded_posting
    if j>12:
        break
             


print "done scraping! writing to file..."

#################################### THIS IS THE WRITING PART
with open("all_results_tripadvisor2.json", 'w') as my_file:                                              #this is how you open a file. the 'w' means we are going to write to it.
    data_to_write = json.dumps(all_postings)                                                #because we have an array, we need to turn it into a string before writing
    my_file.write(data_to_write)                                                            #and finally we write!

