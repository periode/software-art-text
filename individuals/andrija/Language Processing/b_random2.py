## thank you Arantza for this code...
## this is bascially her code 

from textblob import TextBlob       #first, we need to import TextBlob, the package that will help us analyze text
import random
import json

from wordnik import *

# here we set up all we need to get access to the Wordnik API
api_url = 'http://api.wordnik.com/v4'
api_key = 'dc73bd2b889304d23700403b0de048a90e8f5f60a0e42d0f1'
client = swagger.ApiClient(api_key, api_url)

wordsApi = WordsApi.WordsApi(client)                #something
# response = wordsApi.getRandomWords()
response = wordsApi.getRandomWords(limit=100)       #make "response" object, 100 random words

random_words = []
random_paragraph = ""

nouns = []                                  #this is the list where we will store all our nouns
verbs = []                                  #this one is where we will store verbs
adjectives = []

random_nouns = []
random_verbs = []
random_adjectives = []

source = """Friday night and the lights are low,
Looking out for the place to go,
Where they play the right music, getting in the swing,
You come in to look for a king,
Anybody could be that guy,
Night is young and the music's high,
With a bit of rock music, everything is fine,
You're in the mood for a dance,
And when you get the chance...
You are the Dancing Queen, young and sweet, only seventeen
dancing queen, feel the beat from the tambourine
You can dance, you can jive, having the time of your life
See that girl, watch that scene, digging the dancing Queen""" #abba

print "here is original: "
print source

source_processed = TextBlob(source)         #process source in TextBlob

for element in response:                    #
    # print element.word
    random_words.append(element.word)       # add random words to an array, random_words

random_paragraph = " ".join(random_words)   # take the random words, make into a paragraph of random words
# print str(random_paragraph)
# print random_paragraph
random_paragraph_processed = TextBlob(random_paragraph)     #process that paragraph in TextBlob

# PARTS OF SPEECH allows you to get the grammatical role of each 'random' word
for word, tag in random_paragraph_processed.tags:
    # print "word: %s || part-of-speech: %s" % (word, tag)
    if tag == "NN":             #here we are looking for nouns (NN)
        random_nouns.append(word)      #if we find one, we append it to our list
    elif tag == "VB":           #here we look for verbs (VB)
        random_verbs.append(word)
    elif tag == "JJ":           #and here for adjectives
        random_adjectives.append(word)

#### replace text in original paragraph ####
for word, tag in source_processed.tags:

    ## nouns ##
    if tag == 'NN':
		if len(random_nouns) != 0:
			other = random.choice(random_nouns)
			source = source.replace(word, other)

    ## verbs ##
    if tag == 'VB':
    	if len(random_verbs) != 0:
    		other = random.choice(random_verbs)
    		source = source.replace(word, other)

    ## adjectives ##
    if tag == 'JJ':
        if len(random_adjectives) != 0:
            other = random.choice(random_adjectives)
            source = source.replace(word, other)

print "here is random version: "
print '\n'
print source

print "og nouns are"
print nouns
