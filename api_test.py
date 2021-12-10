import requests
import json

host = 'http://127.0.0.1:5000/'

path = 'movie'
url = host + path


name = "/up_comming"
page = 2

r = requests.get(url+name, params={'page':page})
print(json.loads(r.text))

name = "/higher_grade"
page = 1

r = requests.get(url+name, params={'page':page})
print(json.loads(r.text))

name = "/popular_movie"
page = 1

r = requests.get(url+name, params={'page':page})
print(json.loads(r.text))