from textblob import TextBlob
from wordnik import *
import random

# here we set up all we need to get access to the Wordnik API
api_url = 'http://api.wordnik.com/v4'
api_key = 'dc73bd2b889304d23700403b0de048a90e8f5f60a0e42d0f1'
client = swagger.ApiClient(api_key, api_url)
wordsApi = WordsApi.WordsApi(client)
response = wordsApi.getRandomWords(limit=100)

print '\n'
print 'Original Paragraph'
paragraph = """I felt a drift through the wind carrying me across the sands. 
I pondered for quite a while until I realized I was not here. 
I was anywhere but here. 
This was not my place."""


processed_paragraph = TextBlob(paragraph)
print paragraph

random_words = []
random_nouns = []
random_verbs = []
random_adjs = []

for element in response:
	random_words.append(element.word)
rand_sentence = " ".join(random_words)
processed_rand_sentence = TextBlob(rand_sentence)

for word, tag in processed_rand_sentence.tags:

	if tag == "NN":
		random_nouns.append(word)

	elif tag == "VB":
		random_verbs.append(word)

	elif tag == "JJ":
		random_adjs.append(word)

for word, tag in processed_paragraph.tags:

	if tag == 'NN':
		if len(random_nouns) != 0:
			other = random.choice(random_nouns)
			paragraph = paragraph.replace(word, other)

	if tag == 'VB':
		if len(random_verbs) != 0:
			other = random.choice(random_verbs)
			paragraph = paragraph.replace(word, other)

	if tag == 'JJ':
		if len(random_adjs) != 0:
			other = random.choice(random_adjs)
			paragraph = paragraph.replace(word, other)

print '\n'
print 'Generated Paragraph'
print paragraph