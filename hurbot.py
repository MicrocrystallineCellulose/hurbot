import tweepy
import api
import csv

api_key = oygvLjGPxBChmMLtvR8mrmeMb
api_secret = iwIWl4cd38Oha0N9BavITyG8dqhAaLEoHFErr5UaYBECRakO6i

access_token = 1428730744201908225-89EYJZcOwZqI2O8BBtStrwO6zUrs5Q
access_token_secret = l5Kzrnx1XStg8jFI6pUQj5wrEO7Q26KLcPtVOigxvOwfm

print("my twitter bot")

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

try:
    redirect_url = auth.get_authorization_url()
    print("working")
except tweepy.TweepError:
    print('Error! Failed to get request token.')

api = tweepy.API(auth)
quotes = []

with open('C:/Users/llare/downloads/hurquotes.csv', 'rt', encoding = 'utf-8') as csvfile:
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
