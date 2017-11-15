from textblob import TextBlob
import random

source = "I felt as if the world left me like a replacement. It was an evening after working in a factory. I decided to wade through the crowd of artists. I made my way towards the exit."
processed = TextBlob(source)

custom_dictionary = []

for word, pos in processed.tags:
    # print "word: %s - pos: %s" % (word, pos)
    if str(pos) == 'NN':
        # print "possibilities for %s:" % word,

        entry = {
            'word': word,
            'others': []
        }

        for synset in word.get_synsets(pos="n"):
            for syn in synset.lemmas():               #this gets the set of nouns from which our word comes from
                entry['others'].append(syn.name().replace('_', ' '))
                if syn.antonyms():
                    print syn.antonyms()[0].name()
                    entry['others'].append(syn.antonyms()[0].name().replace('_', ' '))


        # print entry['synonyms']
        custom_dictionary.append(entry)

        # print "--"

for token in processed.tokenize():
    for entry in custom_dictionary:
        if token == entry['word']:

            if len(entry['others']) != 0:
                other = random.choice(entry['others'])
                source = source.replace(token, other)

print source
