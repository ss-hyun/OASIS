import requests
import json
import time

host = 'http://127.0.0.1:5000/'

path = 'admin'
url = host + path
name = "/act_in"

p = requests.post(url+name, data="/home/ss/MEI_database/ACT_IN2500.json")
print(p)

p = requests.post(url+name, data="/home/ss/MEI_database/ACT_IN5000.json")
print(p)