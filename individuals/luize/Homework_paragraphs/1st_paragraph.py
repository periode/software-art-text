from textblob import TextBlob
import random

source = "I woke up this morning and saw sunshine outside my window. A new day had arrived. I felt as if the memories from yesterday were slowly fading away. I now need to find a way how to encapsulate them."
processed = TextBlob(source)
print source
custom_dictionary = []


for word, tag in processed.tags:
    if tag == 'NN':

        entry = {               
            'word': word,       
            'others': []        
        }

        for synset in word.get_synsets(pos="n"):
            for syn in synset.lemmas():                                 
                entry['others'].append(syn.name().replace('_', ' '))   
                if syn.antonyms():
                    entry['others'].append(syn.antonyms()[0].name().replace('_', ' '))

        custom_dictionary.append(entry)


for token in processed.tokenize():                      # we need to tokenize it in order to make sure we get each part of the sentences
    for entry in custom_dictionary:                     # then for each token, we go through our custom dictionary
        if token == entry['word']:                      # if we match the word

            if len(entry['others']) != 0:               # and if we actually do have a word to replace it with!
                other = random.choice(entry['others'])  # then we pick a random alternative
                source = source.replace(token, other)   # and we replace it in the source text

print source