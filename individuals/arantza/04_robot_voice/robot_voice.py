#### import modules ####
from textblob import TextBlob
from wordnik import *
import random
import re

#### initialize wordnik ####
api_url = 'http://api.wordnik.com/v4'
api_key = 'a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'
client = swagger.ApiClient(api_key, api_url)
wordApi = WordApi.WordApi(client)

#### initialize and process sentence ####
life_sentence = 'this is the eternal circle of a beautiful life'
death_sentence = 'this is the fleeting circle of the ending death'
processed_sentence = TextBlob(life_sentence)

#### initialize noun lists ####
noun_main = []

#### loop through processed sentence and append nouns to main list ####
for word, tag in processed_sentence.tags:
    if tag == 'NN':

        ## use wordnik to find phrases similar to the noun ##
        noun_phrases = wordApi.getPhrases(word)
        if noun_phrases != None:
            ## append the phrases to the poem list ##
            for phrase in noun_phrases:
                temp = phrase.gram1 + ' ' + phrase.gram2
                noun_main.append(temp)

        ## use wordnik to find definitions of the noun ##
        noun_definitions = wordApi.getDefinitions(word)
        if noun_definitions != None:
            ## append the definitions to the poem list ##
            for definition in noun_definitions:
                noun_main.append(definition.text)

        ## join the nouns into one sentence and clean it ##
        noun_sentence = ", ".join(noun_main)
        noun_sentence = re.sub(' +', ' ', noun_sentence)

#### initialize adjective lists ####
adjective_main = []

#### loop through processed sentence and append adjectives to main list ####
for word, tag in processed_sentence.tags:
    if tag == 'JJ':

        ## use wordnik to find phrases similar to the adjective ##
        adjective_phrases = wordApi.getPhrases(word)
        if adjective_phrases != None:
            ## append the phrases to the poem list ##
            for phrase in adjective_phrases:
                temp = phrase.gram1 + ' ' + phrase.gram2
                adjective_main.append(temp)

        ## use wordnik to find definitions of the adjective ##
        adjective_definitions = wordApi.getDefinitions(word)
        if adjective_definitions != None:
            ## append the definitions to the poem list ##
            for definition in adjective_definitions:
                adjective_main.append(definition.text)

        ## join the nouns into one sentence and clean it ##
        adjective_sentence = ", ".join(adjective_main)
        adjective_sentence = re.sub(' +', ' ', adjective_sentence)

#### clean sentence further by removing 'see synonyms' from string ####
noun_sentence = noun_sentence.replace('See Synonyms', "")
adjective_sentence = adjective_sentence.replace('See Synonyms', "")

#### write to json file ####
with open('life_dataset.txt', 'w') as my_file:
    my_file.write(noun_sentence.encode('utf8') + ' ')
    my_file.write(adjective_sentence.encode('utf8'))
    print 'writing nouns and adjectives to file'
