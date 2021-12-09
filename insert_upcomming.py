import requests
import json
import time

host = 'http://127.0.0.1:5000/'

path = 'admin'
url = host + path


name = "/movie"
p = requests.post(url+name, data="/home/ss/MEI_database/MOVIE_Up_219.json")
print(p)

name = "/movie_officials"
p = requests.post(url+name, data="/home/ss/MEI_database/movie_officials_Up.json")
print(p)


name = "/act_in"
p = requests.post(url+name, data="/home/ss/MEI_database/ACT_IN_Up.json")
print(p)


name = "/directed"
p = requests.post(url+name, data="/home/ss/MEI_database/DIRECTED_Up.json")
print(p)


name = "/genres"
p = requests.post(url+name, data="/home/ss/MEI_database/Genres_Up.json")
print(p)