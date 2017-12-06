from textblob import TextBlob
import random

print '\n'
print 'Original Paragraph'
paragraph = []
with open('cyte.txt', 'r') as f:
    paragraph = [line.strip() for line in f]
    paragraph.append(line)
    str1 = ''.join(paragraph)
    processed_paragraph = TextBlob(str1)

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
		for synset in word.get_synsets(pos='v'):
			for syn in synset.lemmas():
				entry['synonyms'].append(syn.name().replace('_', ' '))

		verbs.append(entry)
	
	elif tag == "JJ":
		entry = {
			'word': word,
			'synonyms': []
		}
		for synset in word.get_synsets(pos='a'):
			for syn in synset.lemmas():
				entry['synonyms'].append(syn.name().replace('_', ' '))

		adjectives.append(entry)


for token in processed_paragraph.tokenize():
	for entry in nouns:

		if token == entry['word']:
			if len(entry['synonyms']) != 0:
				synonym = random.choice(entry['synonyms'])
				str1 = str1.replace(token, synonym)

	for entry in verbs:
		if token == entry['word']:
			if len(entry['synonyms']) != 0:
				synonym = random.choice(entry['synonyms'])
				str1 = str1.replace(token, synonym)

	for entry in adjectives:
		if token == entry['word']:

			if len(entry['synonyms']) != 0:
				synonym = random.choice(entry['synonyms'])
				str1 = str1.replace(token, synonym)
				print token, synonym

print '\n'
print "Generated Paragraph"
print str1