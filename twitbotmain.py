import tweepy
import config
import requests, json

#Get $BTC price

response_API = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
data = response_API.text

pydict = json.loads(data)
BTCVALUE = (pydict['price'])

BTCVALUE = float(BTCVALUE)
f'{BTCVALUE:.2f}'

#Authenticate and send tweet

client = tweepy.Client(config.bearer_token, config.api_key, config.api_secret, config.access_token, config.access_token_secret)

auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

client.create_tweet(text=f"Merde! $BTC is now worth ${BTCVALUE}. Pathetic! Go to sendbtchere.com")