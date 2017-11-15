import requests                                                                            
import bs4                                                                                 
import json                                                                             

all_postings = []                                                                         
currently_scraping_count = 0                                                             

#################################### THIS IS THE REQUEST PART

url_to_scrape = "https://www.teenvogue.com/wellness/nutrition"
our_request = requests.get(url_to_scrape)                                                  
print "requested page sent response code: %s" % our_request.status_code                    


#################################### THIS IS THE PARSING PART


parsed_html = bs4.BeautifulSoup(our_request.text, 'html.parser')

all_results = parsed_html.find_all(class_="feature-item-hed")

for result in all_results:
    
    posting_body = result.find_all(class_="feature-item-link")      
	
    cleaned_posting = posting_body[0].text.replace("QR Code Link to This Post", "").strip() 
	
    currently_scraping_count += 1                                                           
	
    print "scraped posting: %i/%i" % (currently_scraping_count, len(all_results))         
	
    properly_encoded_posting = cleaned_posting.encode('utf-8')                           
	
    all_postings.append(properly_encoded_posting)                                         

print "done scraping! writing to file..."


#################################### THIS IS THE WRITING PART

with open("vogue-results.json", 'w') as my_file:                                             
	
    data_to_write = json.dumps(all_postings)                                               
	
    my_file.write(data_to_write)                                                         