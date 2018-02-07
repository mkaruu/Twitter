from requests_oauthlib import OAuth1Session
import secrets
import json
import nltk 
nltk.download('punkt')

client_key = secrets.client_key
client_secret = secrets.client_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
print (r.text)

python_resp = json.loads(r.text)

sentence = ''
for diction in python_resp:
	diction['statuses'] #find the value for this key then iterate over the list
	sentence += diction['statuses']['text'] 
#print(sentence)

tokens = nltk.word_tokenize(sentence)
print(tokens)