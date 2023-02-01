import snscrape.modules.twitter as sntwitter
import pandas as pd

searchQuery = "kitabisa.com"
tweets = []
tweetLimit = 200

for tweet in sntwitter.TwitterSearchScraper(searchQuery).get_items():

	if len(tweets) == tweetLimit:
		break
	else:
		tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
# print(df)
df.to_csv('user-tweets-kitabisa.csv')
