from textblob import TextBlob


source_text = "Don't tell me the moon is shining; show me the glint of light on broken glass." #chekov

processed_text = TextBlob(source_text)
nouns = []
verbs = []
adjectives = []

print "\n======================\n"

# you can separate the sentence in individual tokens (essentially words)
for word in processed_text.tokenize():
    print word

print "\n======================\n"

# you can find the tags (all the part of sentences of the words
for word, tag in processed_text.tags:
    print "word: %s || part-of-speech: %s" % (word, tag)
    if tag == "NN":
        nouns.append(word)
    elif tag == "VB":
        verbs.append(word)
    elif tag == "JJ":
        adjectives.append(word)
    
print "\n======================\n"

# you can get all the sets of synonyms for specific words
for noun in nouns:
    print "-----------"
    print "-----------"
    print noun
    for synset in noun.get_synsets(pos="n"):
        print "definition: %r" % synset.definition()
        print "lemmas: %r" % synset.lemma_names()
        print "antonyms: ",
        for lemma in synset.lemmas():
            print lemma.antonyms(),
        print ""
        print "hyponyms: %r" % synset.hyponyms()
        print "hypernyms: %r" % synset.hypernyms()

    print "--"
