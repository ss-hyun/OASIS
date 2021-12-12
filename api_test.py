import requests
import json

host = 'http://127.0.0.1:5000/'

path = 'movie'
url = host + path

# name = "/up_comming"
# page = 2

# r = requests.get(url+name, params={'page':page})
# print(json.loads(r.text))

# name = "/higher_grade"
# page = 1

# r = requests.get(url+name, params={'page':page})
# print(json.loads(r.text))

# name = "/popular_movie"
# page = 1

# r = requests.get(url+name, params={'page':page})
# print(json.loads(r.text))

# name = "/participate_officials"
# page = 1
# moid = 11

# r = requests.get(url+name, params={'page':page,'moid':moid})
# print(json.loads(r.text))

name = "/movie_deep"
mvid = 13

r = requests.get(url+name, params={'mvid':mvid})
print(json.loads(r.text))

# name = "/participated_movie"
# page = 1
# mvid = 11

# r = requests.get(url+name, params={'page':page,'mvid':mvid})
# print(json.loads(r.text))


# name = "/participate_deep"
# moid = 884

# r = requests.get(url+name, params={'moid':moid})
# print(json.loads(r.text))