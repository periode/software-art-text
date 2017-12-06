from textblob import TextBlob       #first, we need to import TextBlob, the package that will help us analyze text
import nltk
nltk.download('punkt')

#source_text = "Don't tell me the moon is shining; show me the glint of light on broken glass." #chekov
source_text = "There is also a lot of famous people buried here and they run tours"

processed_text = TextBlob(source_text)      #in order for us to process it, we pass it to TextBlob
nouns = []                                  #this is the list where we will store all our nouns
verbs = []                                  #this one is where we will store verbs
adjectives = []                             #this is where we store adjectives

print "\n======================\n"

# TOKENIZING is the process by which you can separate the sentence in individual tokens (essentially words, suffixes, punctuation)
for word in processed_text.tokenize():
    print word

print "\n======================\n"

# PARTS OF SPEECH allows you to get the grammatical role of each word
for word, tag in processed_text.tags:
    print "word: %s || part-of-speech: %s" % (word, tag)
    if tag == "NN":             #here we are looking for nouns (NN)
        nouns.append(word)      #if we find one, we append it to our list
    elif tag == "VB":           #here we look for verbs (VB)
        verbs.append(word)
    elif tag == "JJ":           #and here for adjectives
        adjectives.append(word)

print "\n======================\n"

# SYNSETS are specific structures related to Wordnet, through which you can get all the sets of related words given a specific word
for noun in nouns:
    print "-----------"
    print "-----------"
    print noun
    for synset in noun.get_synsets(pos="n"):            # get_synsets() returns a list of all the synsets, and we specify we only want the ones that are words
        print "definition: %r" % synset.definition()    # here we get the definition
        print "lemmas: %r" % synset.lemma_names()       # the lemma is the root of the word. for instance, the lemma for 'possibilities' is 'possible'
        print "antonyms: ",
        for lemma in synset.lemmas():                   # for each lemma, we get it's antonym (a lot of words don't have antonyms)
            print lemma.antonyms(),
        print ""
        print "hyponyms: %r" % synset.hyponyms()        # hyponyms are words that are subsets of the current word (animal > human)
        print "hypernyms: %r" % synset.hypernyms()      # hypernyms are words that are supersets of the current word (human > being)

    print "--"
