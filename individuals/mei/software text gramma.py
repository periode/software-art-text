from textblob import TextBlob
import random


"""
this is our grammar, it represents the structure of one or more sentences
we are going to use it as a reference to generate concrete sentences.

 You will end up on a tree lined path, 
 and as you emerge onto the board walk,
 Manhattan will appear 

some abbreviations are as follows:
    S: sentence
    NP: noun phrase
    VP: verb phrase
    N: noun
    V: verb
    J: adjective
    PP: preposition
"""

my_grammar = {
        "S": ["NP VP", "and as N1 emerges onto the ADJ N2"],                              # the left part is called an axiom
        "NP": ["the N1", "a N1"],                    # the right part is a list of which elements that axiom is made of
        "VP": ["V3 NP", "will end up in the NP3", "will appear"],                       # notice how the list on the left sometimes contains other axioms
        "N1": ["hope",  "tree",  "love", "breeze","gravity"],
        "N2": ["bridge", "distance",  "path", "truth",  "memory","lie"],
        "NP3":["N1 Ved N2"],
        "V": ["stand", "hear", "tell", "escape", "tear"],
        "V3": ["stands", "hears", "tells", "shows"],
        "Ved": ["filled", "lined","lit", "covered","coated"],
        "ADJ": ["broad", "fat", "trembling", "fever", "shining","sharp","deep","chrispy"]
        }


# this is the function that is going to generate a sentence.
# its arguments are a grammar (the rules to follow) and an axiom (the starting point)
def write_a_sentence(grammar, axiom):

    sentence = list()                                               #we start by creating a list which will store all the words for our sentence

    if axiom in grammar:                                            # if we find one of the axioms (such as NP, V, etc.) as a key in our grammar
        expansion = random.choice(grammar[axiom])                   # then we pick one random item from the list on the left side of the corresponding axiom

        for token in expansion.split():                             # we split the element in separate tokens (e.g. "the N" becomes ["the", "N"]) and we can then look for "N"
            sentence.extend(write_a_sentence(grammar, token))       # if we've found an axiom, we call our function again to dive deeper into our grammar
    else:
        sentence.append(axiom)                                      # until we find nothing, in which case we will append the current axiom (which will be a word, instead of something like "N", or "VP")

    return sentence                                                 # and we return all that we've found!


for i in range(0, 15):                                               # this is how you write a for loop in python
    words = write_a_sentence(my_grammar, "S")                       # we want a write a sentence using my_grammar defined above, and with the starting point "S"
    my_sentence = " ".join(words)                                   # because it returns a list, we need to join all elements with a space
    print my_sentence + "."                                         # and we print it!
