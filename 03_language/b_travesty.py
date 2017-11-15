"""
in this script, we take an input sentence, and we replace each of the nouns with their synonyms
"""

from textblob import TextBlob
import random

source = "I felt as if the world left me like a replacement. It was an evening after working in a factory. I decided to wade through the crowd of artists. I made my way towards the exit."
processed = TextBlob(source)

custom_dictionary = []

for word, tag in processed.tags:
    if tag == 'NN':

        entry = {               # each of our entries in our dictionary
            'word': word,       # has the initial word
            'others': []        # as well as a list of other possibilities
        }

        for synset in word.get_synsets(pos="n"):
            for syn in synset.lemmas():                                 # here we loop through the list of lemmas that are related to the current noun
                entry['others'].append(syn.name().replace('_', ' '))    # we also replace any possible '_' character with a ' ' space character when we add it to our list of other possibilities
                if syn.antonyms():
                    entry['others'].append(syn.antonyms()[0].name().replace('_', ' '))
        
        custom_dictionary.append(entry) # then we add the entry to our dictionary


# this the part where we actually replace the source text
for token in processed.tokenize():                      # we need to tokenize it in order to make sure we get each part of the sentences
    for entry in custom_dictionary:                     # then for each token, we go through our custom dictionary
        if token == entry['word']:                      # if we match the word

            if len(entry['others']) != 0:               # and if we actually do have a word to replace it with!
                other = random.choice(entry['others'])  # then we pick a random alternative
                source = source.replace(token, other)   # and we replace it in the source text

print source
