from wordnik import *

# here we set up all we need to get access to the Wordnik API
api_url = 'http://api.wordnik.com/v4'
api_key = 'a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5'
client = swagger.ApiClient(api_key, api_url)

print ""
print "------------------------"
print "WORD PHRASES"
#### API EXAMPLE: Word http://developer.wordnik.com/docs.html#!/word
wordApi = WordApi.WordApi(client)                   # create the api endpoint
response = wordApi.getPhrases('hope')               # ask for the phrases that go with our word
for element in response:                            # because we get a list, we need to loop through
    print "%s %s" % (element.gram1, element.gram2)  # you can get the format of the response on the documentation (here, it's an object with the fields `gram1` and `gram2`)

print ""
print "------------------------"
print "WORD DEFINITIONS"
response = wordApi.getDefinitions('hope')
for element in response:
    print element.text

print ""
print "------------------------"
print "WORD DEFINITIONS"
response = wordApi.getRelatedWords('hope')
for types in response:
    print "relationship: %s" % types.relationshipType
    for suggested in types.words:
        print suggested
    print "---"

print ""
print "------------------------"
print "RANDOM WORDS"
#### API EXAMPLE: Words http://developer.wordnik.com/docs.html#!/words
wordsApi = WordsApi.WordsApi(client)
response = wordsApi.getRandomWords()
for element in response:
    print element.word
