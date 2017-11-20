#### import modules ####
from textblob import TextBlob
import random
import re

#### import twitter database into program ####
word_database = []
with open('final_dataset.txt') as my_file:
    word_database = my_file.read().split()

#### join and process words ####
database_sentence = " ".join(word_database)
new_database_sentence = re.sub(r'http\S+', '', database_sentence)
processed_database_sentence = TextBlob(new_database_sentence)

#### my_grammar directory ####
my_grammar = {
        "S": ["NP VP NP"],
        "NP": ["N", "det N", "det N"],
        "det": ["the J"],
        "VP": ["V", "can V"],
        "N": [""],
        "V": [""],
        "J": [""]
}

#### append words into dictionary according to their type ####
for word, tag in processed_database_sentence.tags:

    ## nouns ##
    if tag == "NN":
        my_grammar['N'].append(word)

    ## verbs ##
    elif tag == 'VB':
        my_grammar['V'].append(word)

    ## adjectives ##
    elif tag == 'JJ':
        my_grammar['J'].append(word)

#### function for writing a sentence ####
def write_a_sentence(grammar, axiom):
    sentence = list()
    if axiom in grammar:
        expansion = random.choice(grammar[axiom])
        for token in expansion.split():
            sentence.extend(write_a_sentence(grammar, token))
    else:
        sentence.append(axiom)
    return sentence

#### outputing the final poem ####
for i in range(0, 2):
    words_1 = write_a_sentence(my_grammar, "NP")
    my_sentence_1 = " ".join(words_1)
    print my_sentence_1 + "."

for i in range(0, 5):
    words_2 = write_a_sentence(my_grammar, 'S')
    my_sentence_2 = " ".join(words_2)
    print my_sentence_2 + "."