from textblob import TextBlob
import random

print '\n'
print 'Original Paragraph'
paragraph = """Tell me where you want to strike, 
Whether its here or there,
You can really strike me everywhere,
But know this you wretched fool,
If it is big, it amounts to the suffering,
And if it is small, it is of how little you cared,
So you can have my body,
But you are always going to be scared of what is inside,
Because if you weren't,
You would strike me at the heart,
But you never had yours in the first place.""" #Ali
processed_paragraph = TextBlob(paragraph)
print paragraph

nouns = []
verbs = []
adjectives = []

for word, tag in processed_paragraph.tags:
	
	if tag == 'NN':
		entry = {
			'word': word,
			'synonyms': []
		}
		for synset in word.get_synsets(pos='n'):
			for syn in synset.lemmas():
				entry['synonyms'].append(syn.name().replace('_', ' '))

		nouns.append(entry)
	
	elif tag == "VB":
		entry = {
			'word': word,
			'synonyms': []
		}
		for synset in word.get_synsets(pos='n'):
			for syn in synset.lemmas():
				entry['synonyms'].append(syn.name().replace('_', ' '))

		verbs.append(entry)
	
	elif tag == "JJ":
		entry = {
			'word': word,
			'synonyms': []
		}
		for synset in word.get_synsets(pos='n'):
			for syn in synset.lemmas():
				entry['synonyms'].append(syn.name().replace('_', ' '))

		adjectives.append(entry)

for token in processed_paragraph.tokenize():

	for entry in nouns:
		if token == entry['word']:

			if len(entry['synonyms']) != 0:
				synonym = random.choice(entry['synonyms'])
				paragraph = paragraph.replace(token, synonym)

	for entry in verbs:
		if token == entry['word']:

			if len(entry['synonyms']) != 0:
				synonym = random.choice(entry['synonyms'])
				paragraph = paragraph.replace(token, synonym)

	for entry in adjectives:
		if token == entry['word']:

			if len(entry['synonyms']) != 0:
				synonym = random.choice(entry['synonyms'])
				paragraph = paragraph.replace(token, synonym)

print '\n'
print "Generated Paragraph"
print paragraph