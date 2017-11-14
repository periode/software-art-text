import json                                     #we are going to use json

input_file = ""

with open(input_file, 'r') as my_file:              #we open a file
    retrieved_postings = json.load(my_file)         #we use the json.load() function to make sense of that JSON
    with open("full_poem.txt", 'w') as my_poem:     #we open a new file
        for posting in retrieved_postings:          #go through each array
            my_poem.write(posting.encode('utf-8'))  #write each line, encoded as UTF8
