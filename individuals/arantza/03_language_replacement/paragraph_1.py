#### import modules ####
from textblob import TextBlob
import random

#### initialize and process sentence ####
print '\n'
print 'FIRST PARAGRAPH'
paragraph = '''let me sail to the voice that is as lifeless as the sun. 
There is no death in this paradise.
Nor happiness in this hell.'''
processed_paragraph = TextBlob(paragraph)
print paragraph

#### initialize lists for synonyms ####
nouns = []
verbs = []
adjectives = []

#### create entries in a dictionary with original word and synonyms ####
for word, tag in processed_paragraph.tags:
	
	## nouns ##
	if tag == 'NN':
		entry = {
			'word': word,
			'synonyms': []
		}
		## loop through list of synonyms in wordnet and append ##
		for synset in word.get_synsets(pos='n'):
			for syn in synset.lemmas():
				entry['synonyms'].append(syn.name().replace('_', ' '))

		## append synonyms to noun dictionary ##
		nouns.append(entry)
	
	## verbs ##
	elif tag == "VB":
		entry = {
			'word': word,
			'synonyms': []
		}
		## loop through list of synonyms in wordnet and append ##
		for synset in word.get_synsets(pos='v'):
			for syn in synset.lemmas():
				entry['synonyms'].append(syn.name().replace('_', ' '))

		## append synonyms to verb dictionary
		verbs.append(entry)
	
	## adjectives ##
	elif tag == "JJ":
		entry = {
			'word': word,
			'synonyms': []
		}
		## loop through list of synonyms in wordnet and append ##
		for synset in word.get_synsets(pos='j'):
			for syn in synset.lemmas():
				entry['synonyms'].append(syn.name().replace('_', ' '))

		## append synonyms to verb dictionary
		adjectives.append(entry)

#### replace text in original sentence ####
for token in processed_paragraph.tokenize():

	## nouns ##
	for entry in nouns:
		if token == entry['word']:
			if len(entry['synonyms']) != 0:
				synonym = random.choice(entry['synonyms'])
				paragraph = paragraph.replace(token, synonym)

	## verbs ##
	for entry in verbs:
		if token == entry['word']:
			if len(entry['synonyms']) != 0:
				synonym = random.choice(entry['synonyms'])
				paragraph = paragraph.replace(token, synonym)

	## adjectives ##
	for entry in adjectives:
		if token == entry['word']:
			if len(entry['synonyms']) != 0:
				synonym = random.choice(entry['synonyms'])
				paragraph = paragraph.replace(token, synonym)

print '\n'
print "SYNONYM PARAGRAPH"
print paragraph