import requests
import json
import time

host = 'http://127.0.0.1:5000/'

path = 'admin'
url = host + path


name = "/movie"
p = requests.post(url+name, data="/home/ss/MEI_database/UPCOMING_220.json")
print(p)

name = "/movie_officials"
p = requests.post(url+name, data="/home/ss/MEI_database/UP_movie_officials.json")
print(p)


name = "/act_in"
p = requests.post(url+name, data="/home/ss/MEI_database/UP_ACTIN.json")
print(p)


name = "/directed"
p = requests.post(url+name, data="/home/ss/MEI_database/UP_DIRECTED.json")
print(p)


name = "/genres"
p = requests.post(url+name, data="/home/ss/MEI_database/UPCOMING_Genres.json")
print(p)