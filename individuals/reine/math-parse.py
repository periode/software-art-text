import requests                                                                       
import bs4                                                                           
import json

all_postings = []                                                                         
currently_scraping_count = 0                                                             

####################################

url_to_scrape = "https://www.reddit.com/r/MathHelp/comments/766hdt/multivariable_calculus_im_struggling_with_a/"
our_request = requests.get(url_to_scrape)                                                  
print "requested page sent response code: %s" % our_request.status_code 

####################################

parsed_html = bs4.BeautifulSoup(our_request.text, 'html.parser')

all_results = parsed_html.find_all(class_="usertext")

for result in all_results:
    
    posting_body = result.find_all('p')      
	
    cleaned_posting = posting_body[0].text.replace("", "").strip() 
	
    currently_scraping_count += 1                                                           
	
    print "scraped posting: %i/%i" % (currently_scraping_count, len(all_results))         
	
    properly_encoded_posting = cleaned_posting.encode('utf-8')                           
	
    all_postings.append(properly_encoded_posting)              

####################################

with open("quantum.json", 'w') as my_file:                                             
	
    data_to_write = json.dumps(all_postings)                                               
	
    my_file.write(data_to_write)                                                         