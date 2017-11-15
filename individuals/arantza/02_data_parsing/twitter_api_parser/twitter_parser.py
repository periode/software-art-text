#### import modules ####
import json
from twitter import *

#### initialize variables to access the twitter API ####
ACCESS_TOKEN = '781473744187453440-cLTyH1wI1We44STQyycwNTYkBr6eSnL'
ACCESS_SECRET = 'n6NxbWnM3duSbY5TzrlGfGJXcPvfnxOYvIU1jpJtU9P51'
CONSUMER_KEY = 'KUppimNiOu2u6RsB0ATUZYvST'
CONSUMER_SECRET = 'aXmItSxETrNPg8tm1LFGr0TYVLUD4jYwWY7uqgykqlBIyUvvvR'
twitter = Twitter(
    auth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
)

#### initialize accounts ####
user_account_1 = 'sosadtoday'
user_account_2 = 'sad'

#### initialize lists ####
all_tweets_1 = []
all_tweets_2 = []

#### parse twitter websites with API ####
results_1 = twitter.statuses.user_timeline(screen_name = user_account_1, count = 200)
for tweet in results_1:
    tweet_text = tweet['text'].encode('ascii', 'ignore')
    all_tweets_1.append(tweet_text)
print 'done scraping first account!'

results_2 = twitter.statuses.user_timeline(screen_name = user_account_2, count = 200)
for tweet in results_2:
    tweet_text = tweet['text'].encode('ascii', 'ignore')
    all_tweets_2.append(tweet_text)
print 'done scraping second account!'

#### write to json file ####
with open('tweet_file_1.json', 'w') as my_file:
    tweets_to_write = json.dumps(all_tweets_1)
    my_file.write(tweets_to_write)
    print 'writing tweets to first json file.'

with open('tweet_file_2.json', 'w') as my_file:
    tweets_to_file = json.dumps(all_tweets_2)
    my_file.write(tweets_to_file)
    print 'writing tweets to second json file.'

#### write to text file ####
with open('tweet_file_1.json', 'r') as my_file:
    retrieved_tweets = json.load(my_file)
    with open('tweet_poem_1.txt', 'w') as my_poem:
        for tweet in retrieved_tweets:
            my_poem.write(tweet.encode('utf8') + '\n')
    print 'writing tweets to first poem file.'

with open('tweet_file_2.json', 'r') as my_file:
    retrieved_tweets = json.load(my_file)
    with open('tweet_poem_2.txt', 'w') as my_poem:
        for tweet in retrieved_tweets:
            my_poem.write(tweet.encode('utf8') + '\n')
    print 'writing tweets to second poem file.'

#### merge two datasets together ####
files = ['tweet_poem_1.txt', 'tweet_poem_2.txt']
with open('final_dataset.txt', 'w') as my_file:
    for fname in files:
        with open(fname) as in_file:
            for line in in_file:
                my_file.write(line)
print 'finished merging datasets.'
