#### import modules ####
from textblob import TextBlob
from wordnik import *
import random

#### initialize wordnik ####
api_url = 'http://api.wordnik.com/v4'
api_key = 'a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'
client = swagger.ApiClient(api_key, api_url)
wordApi = WordApi.WordApi(client)

#### initialize and process sentence ####
print '\n'
print 'SECOND PARAGRAPH'
paragraph = '''let me sail to the voice that is as lifeless as the sun. 
There is no death in this paradise.
Nor happiness in this hell.'''
processed_paragraph = TextBlob(paragraph)
print paragraph

#### intialize lists for random nouns, verbs, and adjectives ####
random_words = []
random_nouns = []
random_verbs = []
random_adjs = []

#### use wordnik to find random words ####
wordsApi = WordsApi.WordsApi(client)
response = wordsApi.getRandomWords(limit=100)

#### append and process words in sentence ####
for element in response:
	random_words.append(element.word)
rand_sentence = " ".join(random_words)
processed_rand_sentence = TextBlob(rand_sentence)

#### append words according to their type ####
for word, tag in processed_rand_sentence.tags:

	## nouns ##
	if tag == "NN":
		random_nouns.append(word)

	## verbs ##
	elif tag == "VB":
		random_verbs.append(word)

	## adjectives ##
	elif tag == "JJ":
		random_adjs.append(word)

#### replace text in original paragraph ####
for word, tag in processed_paragraph.tags:

	## nouns ##
	if tag == 'NN':
		if len(random_nouns) != 0:
			other = random.choice(random_nouns)
			paragraph = paragraph.replace(word, other)

	## verbs ##
	if tag == 'VB':
		if len(random_verbs) != 0:
			other = random.choice(random_verbs)
			paragraph = paragraph.replace(word, other)

	## adjectives ##
	if tag == 'JJ':
		if len(random_adjs) != 0:
			other = random.choice(random_adjs)
			paragraph = paragraph.replace(word, other)

print '\n'
print 'RANDOM PARAGRAPH'
print paragraph