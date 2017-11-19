#########Consolidating all page jsons into one database

import json
import random 
from time import sleep 

full_script = []

with open("page1.json", 'r') as file1: 
    retrieved_postings = json.load(file1)
    page1 = retrieved_postings	

with open("page2.json", 'r') as file1: 
    retrieved_postings = json.load(file1)
    page2 = retrieved_postings
	

with open("page3.json", 'r') as file1: 
    retrieved_postings = json.load(file1)
    page3 = retrieved_postings	
	

with open("page4.json", 'r') as file1: 
    retrieved_postings = json.load(file1)
    page4 = retrieved_postings	

	
with open("page5.json", 'r') as file1: 
    retrieved_postings = json.load(file1)
    page5 = retrieved_postings	
	

full_script = page1+page2+page3+page4+page5
	
#print full_script 

with open("database-twenty-and.json", 'w') as my_file:                                             
    data_to_write = json.dumps(full_script)                                               
    my_file.write(data_to_write)                                                         