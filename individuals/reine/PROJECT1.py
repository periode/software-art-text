import requests                                                       import bs4                                                           import json

all_postings = []                                                                         
currently_scraping_count = 0                                                             

####################################

url_to_scrape = "https://www.google.com/search?q=I%27m+20+and&ei=yZEMWpeyBcfQwQL_6ZiYDA&start=40&sa=N&biw=1292&bih=755"
our_request = requests.get(url_to_scrape)                                                  
print "requested page sent response code: %s" % our_request.status_code                    

####################################

parsed_html = bs4.BeautifulSoup(our_request.text, 'html.parser')

all_results = parsed_html.find_all(class_="g")

for result in all_results:
    
    posting_body = result.find_all(class_="r")      
	
    cleaned_posting = posting_body[0].text.replace("-", "").strip() 
	
    currently_scraping_count += 1                                                           
	
    print "scraped posting: %i/%i" % (currently_scraping_count, len(all_results))         
	
    properly_encoded_posting = cleaned_posting.encode('utf-8')                           
	
    all_postings.append(properly_encoded_posting)                                         

####################################

#repeated process for pages 1-5 for about 50 headlines

with open("page5.json", 'w') as my_file:                                 
    data_to_write = json.dumps(all_postings)                                               
    my_file.write(data_to_write)                                                         