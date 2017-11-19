import json

input_file = "quantum.json"

with open(input_file, 'r') as my_file:
    retrieved_postings = json.load(my_file)
    with open("quantum.txt", 'w') as my_poem:
        for posting in retrieved_postings:
            my_poem.write(posting.encode('utf-8'))