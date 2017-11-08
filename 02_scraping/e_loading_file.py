import json                                     #we are going to use json

with open("all_results.json", 'r') as my_file:  #we open a file
    retrieved_postings = json.load(my_file)     #we use the json.load() function to make sense of that JSON

    print "printing all postings as an array:"
    for posting in retrieved_postings:          #now we have an array again!
        print posting                           #so might as well print all elements in the array
