import requests
import json
import time

host = 'http://127.0.0.1:5000/'

path = 'admin'
url = host + path
name = "/genres"

p = requests.post(url+name, data="/home/ss/MEI_database/M_GENRES1.json")
print(p)

p = requests.post(url+name, data="/home/ss/MEI_database/M_GENRES2.json")
print(p)

p = requests.post(url+name, data="/home/ss/MEI_database/M_GENRES3.json")
print(p)

p = requests.post(url+name, data="/home/ss/MEI_database/M_GENRES4.json")
print(p)

p = requests.post(url+name, data="/home/ss/MEI_database/M_GENRES5.json")
print(p)

p = requests.post(url+name, data="/home/ss/MEI_database/M_GENRES6.json")
print(p)

p = requests.post(url+name, data="/home/ss/MEI_database/M_GENRES7.json")
print(p)

p = requests.post(url+name, data="/home/ss/MEI_database/M_GENRES8.json")
print(p)

p = requests.post(url+name, data="/home/ss/MEI_database/M_GENRES9.json")
print(p)