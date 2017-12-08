from textblob import TextBlob
from textblob.wordnet import ADJ

from wordnik import *
import markov

import random
import re

import sys
import getopt

# Globals
mode = ''
input = ''
output = ''
relative = False
nGram = 10
seed = None
mMax = 500

api_url = 'http://api.wordnik.com/v4'
api_key = 'a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'
client = swagger.ApiClient(api_key, api_url)

# Take input
try:
    opts, args = getopt.getopt(sys.argv[1:], "srgmlhi:o:n:", ['seed=', 'max='])
except getopt.GetoptError:
    print("Wrong option!")
    sys.exit()

for opt, arg in opts:
    if opt == '-s':
        mode = 'syn'
    elif opt == '-r':
        mode = 'rand'
    elif opt == '-g':
        mode = 'gram'
    elif opt == '-m':
        mode = 'mark'
    elif opt == '-l':
        relative = True
    elif opt == '--seed':
        seed = arg
    elif opt == '--max':
        mMax = int(arg)
    elif opt == '-i':
        input = arg
    elif opt == '-o':
        output = arg
    elif opt == '-n':
        nGram = int(arg)
    elif opt == '-h':
        print('''HELP
        -s           : Synonym replacement mode
        -r           : Random replacement mode
        -g           : Grammar generation mode
        -m           : Markov chain mode
        -l           : Enable relative sampling for grammar mode
        --seed [arg] : Markov chain seed
        --max [arg]  : Markov chain max length
        -n [arg]     : Set n-gram number for Markov chain mode
        -i [arg]     : Path to input text file
        -o [arg]     : Path to output text file''')
        sys.exit()

if mode == '' or input == '' or output == '':
    print("Invalid options!")
    sys.exit()

# Function to match several verb conjugations yay
def matchVerb(tag):
    vTag = re.compile(r'VB.')
    if vTag.match(tag) is not None:
        return True
    return False

# Helper to add synonyms + antonyms to an entry from a given synset
def addSynAnt(wrd, ent, syns):
    for syn in syns.lemmas():
        ent[wrd].append(syn.name().replace('_', ' '))
                    
        if syn.antonyms():
            for ant in syn.antonyms():
                ent[wrd].append(ant.name().replace('_', ' '))

# Replaces words from input with synonims based on synsets
def synReplace(iFile, oFile):
    print("Processing input...")
    iText = iFile.read()
    iProcessed = TextBlob(iText)

    print(iProcessed.tags)

    # Store entries in a dictionary (word : syn/antonyms)
    entries = {}

    print("Adding synsets to our dictionary...")
    for word, tag in iProcessed.tags:
        try:
            dummy = entries[word]
            continue
        except KeyError:
            entries[word] = []

        if tag == 'NN':      
            for synset in word.get_synsets(pos="n"):
                addSynAnt(word, entries, synset)

        elif tag == 'JJ':
            for synset in word.get_synsets(pos="a"):
                addSynAnt(word, entries, synset)

        elif matchVerb(tag):
            for synset in word.get_synsets(pos="v"):
                addSynAnt(word, entries, synset)

        elif tag == 'RB':
            for synset in word.get_synsets(pos="r"):
                addSynAnt(word, entries, synset)

        else:
            continue

    keys = list(entries.keys())

    # Replace original words with random syn/antonyms
    for token in iProcessed.tokenize():
        for key in keys:
            if token == key:
                if len(entries[key]) != 0:
                    other = random.choice(entries[key])
                    print("Replacing", token, "with", other)

                    replacer = re.compile(r'' + token + r'(?!\w)')
                    print(replacer.search(iText))
                    iText = replacer.sub(other, iText)

    oFile.write(iText)

# Function to replace words with random words of the same Part-of-Speech
def randReplace(iFile, oFile):
    print("Acquiring random words...")
    api = WordsApi.WordsApi(client)
    response = api.getRandomWords()

    randomWords = ""
    for element in response:
        randomWords += element.word
        randomWords += " "

    print("Processing input file...")
    iText = iFile.read()
    iProcessed = TextBlob(iText)
    randProcessed = TextBlob(randomWords)
    randDict = {}

    print("Building random dictionary...")
    for word, tag in randProcessed.tags:
        try:
            randDict[tag].append(word)
        except KeyError:
            randDict[tag] = [word]
    
    print("Replacing with random words...")
    for word, tag in iProcessed.tags:
        newWord = ''
        try:
            newWord = random.choice(randDict[tag])
        except KeyError:
            continue
        
        iText = iText.replace(word, newWord)

    oFile.write(iText)

# Helper to make sentence recursively (#ItsJustPierresCode)
def makeSentence(gram, axiom):
    sentence = list()

    if axiom in gram:
        expansion = random.choice(gram[axiom])

        for token in expansion.split(" "):
            sentence.extend(makeSentence(gram, token))
    else:
        sentence.append(axiom)

    return sentence

# Helper to populate a grammar dictionary from the words found in an input file
def populateGrammar(gram, inp, relative = False):
    print("Populating grammar with input file data...")
    # Relative = True keeps appending words if they appear multiple times
    # Thus, more frequent words become pore likely to be used
    print("Relative frequencies:", relative)
    pInp = TextBlob(inp)

    for word, tag in pInp.tags:
        if tag in gram:
            if word not in gram[tag] or relative:
                gram[tag].append(word)
    print("Done populating!")


def gramGenerate(iFile, oFile):
    # Grammar is based on this simple poem

    #base = '''roses are red
    # violets are blue
    # take this one poem
    # and make it anew'''

    #pBase = TextBlob(base)
    #print(pBase.tags)
    #return

    # Define our branching axioms but leave terminating axioms empty to populate later
    grammar = {
        "STZ"  : ["VRS1 \n VRS1 \n VRS2 \n VRS3"],
        "VRS1" : ["NNS are JJ", "NNS VBP RB"],
        "VRS2" : ["VB DT JJ NN", "VB DT CD NN"],
        "VRS3" : ["CC VB PRP RB", "CC make PRP VB"],
        "VB"   : [],
        "VBP"  : [],
        "NN"   : [],
        "NNS"  : [],
        "DT"   : [],
        "JJ"   : [],
        "RB"   : [],
        "PRP"  : [],
        "CC"   : [],
        "CD"   : []
        }

    iText = iFile.read()
    populateGrammar(grammar, iText, relative)

    print("Building our output...")
    oText = " ".join(makeSentence(grammar, "STZ"))
    oFile.write(oText)

def makeMarkov(iFile, oFile):
    iText = iFile.read();

    print("Building model...")
    model = markov.build_model(iText, nGram);
    print("Assembling output...")
    oText = ''.join(markov.generate(model, nGram, seed, mMax))

    oFile.write(oText)

# Open files and run appropriate function based on options given
with open(input, "r") as inp, open(output, "w") as out:
    print("Input:", input)
    print("Output:", output)
    if mode == 'syn':
        print("\n==== SYNONYM REPLACEMENT ====\n")
        synReplace(inp, out)
    elif mode == 'rand':
        print("\n==== RANDOM REPLACEMENT ====\n")
        randReplace(inp, out)
    elif mode == 'gram':
        print("\n==== CONTEXT-FREE GRAMMAR ====\n")
        gramGenerate(inp, out)
    elif mode == 'mark':
        print("\n==== MARKOV CHAIN ====\n")
        makeMarkov(inp, out)

print("All done! :D")