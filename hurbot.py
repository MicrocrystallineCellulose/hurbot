import tweepy
import random
import csv

api_key = 'paste key in between quote'
api_secret = 'paste key in between quote'

access_token = 'paste key in between quote'
access_token_secret = 'paste key in between quote'

print("my twitter bot")

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)
quotes = []

with open('C:/Users/llare/Downloads/hurquotes.csv', 'rt', encoding = 'unicode_escape') as csvfile:
    lines = csv.reader(csvfile)
    for line in lines:
        print(len(line[0]))
        if len(line[0]) < 280:
            quotes.append(line[0])

for x in range(len(quotes)):
    quotes[x] = quotes[x].replace("\n", " ")
    print(quotes[x])

selection = random.randint(0,len(quotes))
tweet = quotes[selection]
print("final: ", tweet)
api.update_status(tweet)
