from textblob import TextBlob       #first, we need to import TextBlob, the package that will help us analyze text
import random
import json

# "No matter how hard I try, you keep pushing me aside, and I can't break through there's no talking to you, So sad that you're leaving, Takes time to believe it, But after all is said and done, You're going to be the lonely one, oh oh. Do you believe in life after love? I can feel something inside me say I really don't think you're strong enough, no." #cher

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
processed = TextBlob(source)
print source
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
                if syn.hyponyms():
                    entry['others'].append(syn.antonyms()[0].name().replace('_', ' '))

        custom_dictionary.append(entry) # then we add the entry to our dictionary


# this the part where we actually replace the source text
for token in processed.tokenize():                      # we need to tokenize it in order to make sure we get each part of the sentences
    for entry in custom_dictionary:                     # then for each token, we go through our custom dictionary
        if token == entry['word']:                      # if we match the word

            if len(entry['others']) != 0:               # and if we actually do have a word to replace it with!
                other = random.choice(entry['others'])  # then we pick a random alternative
                source = source.replace(token, other)   # and we replace it in the source text
print ""
print source
