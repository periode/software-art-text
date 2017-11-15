#### import modules ####
import requests
import bs4
import json

#### initialize lists #####
all_tweets = []
all_retweets = []
scraping_count = 0

#### initialize request ####
url = "https://twitter.com/sosadtoday"
response = requests.get(url)
print "requested page sent response code: %s" % response.status_code

#### parse website ####
soup = bs4.BeautifulSoup(response.text, 'html.parser')
tweets = soup.find_all(class_= 'js-stream-item')

for tweet in tweets:
    if tweet.find(class_='tweet-text'):
        tweet_text = tweet.find(class_= 'tweet-text').text.encode('utf8').strip()
        all_tweets.append(tweet_text)
        retweets_text = tweet.find(class_= 'ProfileTweet-action--retweet').text.strip()
        all_retweets.append(retweets_text)
        scraping_count += 1
        print "scraping count is %d" % scraping_count
    else:
        continue
print "done scraping!"

#### write to file ####
with open("all_tweets.json", 'w') as my_file:
    tweets_to_write = json.dumps(all_tweets)
    my_file.write(tweets_to_write)
    print "writing tweets to first file."

with open("all_retweets.json", 'w') as my_file:
	retweets_to_write = json.dumps(all_retweets)
	my_file.write(retweets_to_write)
	print "writing retweets to second file."
