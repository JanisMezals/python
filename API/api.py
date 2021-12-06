import requests
response = requests.get('https://random-word-api.herokuapp.com/word?number=10')
       

print(response.text)

#with open 
#print(response.ok)
#print(response.headers)

import json

#def random_word():
#    """request one random word from API. If len of word at least MIN_LEN letters, return it (str). Otherwise, request another."""
#    while True:
 #       r = requests.get('https://random-word-api.herokuapp.com/word', {'number' : 1})
#        r.raise_for_status()
#        word = r.json()[0]
 #       if len(word) >= MIN_LEN:
 #           return word