from wordnik import *

# here we set up all we need to get access to the Wordnik API
api_url = 'http://api.wordnik.com/v4'
api_key = 'dc73bd2b889304d23700403b0de048a90e8f5f60a0e42d0f1'
client = swagger.ApiClient(api_key, api_url)


source = "My name is Luize. I like looking at stars. I have a independent personality."
wordsApi = WordsApi.WordsApi(client)
response = wordsApi.getRandomWords()
for element in response:
    print "My name is %s." %(element.word)
    print "I like %s." %(element.word)
    print "I have a %s." %(element.word)