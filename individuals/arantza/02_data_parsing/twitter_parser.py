#### import modules ####
import json
from twitter import *

#### initialize variables ####
user_account = 'sosadtoday'
scraping_count = 0

#### initialize list ####
all_tweets = []

#### initialize variables that contain my credentials to access the twitter API ####
ACCESS_TOKEN = '781473744187453440-cLTyH1wI1We44STQyycwNTYkBr6eSnL'
ACCESS_SECRET = 'n6NxbWnM3duSbY5TzrlGfGJXcPvfnxOYvIU1jpJtU9P51'
CONSUMER_KEY = 'KUppimNiOu2u6RsB0ATUZYvST'
CONSUMER_SECRET = 'aXmItSxETrNPg8tm1LFGr0TYVLUD4jYwWY7uqgykqlBIyUvvvR'

#### initialize twitter ####
twitter = Twitter(
    auth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
)

#### parse twitter website with API ####
results = twitter.statuses.user_timeline(screen_name = user_account, count = 200)
for tweet in results:
    tweet_text = tweet['text'].encode('ascii', 'ignore')
    all_tweets.append(tweet_text)
    scraping_count += 1
    print 'scraping count is %d' % scraping_count
print 'done scraping!'

#### write to json file ####
with open('tweet_file.json', 'w') as my_file:
    tweets_to_write = json.dumps(all_tweets)
    my_file.write(tweets_to_write)
    print 'writing tweets to tweet file.'

#### write to text file ####
input_file = "tweet_file.json"
with open(input_file, 'r') as my_file:
    retrieved_tweets = json.load(my_file)
    with open('tweet_poem.txt', 'w') as my_poem:
        for tweet in retrieved_tweets:
            my_poem.write(tweet.encode('utf8') + "\n")
    print 'writing tweets to poem file'
