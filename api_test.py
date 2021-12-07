import requests

host = 'http://127.0.0.1:5000/'

path = 'admin'
url = host + path

r = requests.get(url)
print(r.text)

movie = { 'Movie_id': 77888777, 'Title':'"apitest"', 'Release_date': '19970926', 'Running_time':136, 'Movie_rating':'"12"' }





#p = requests.post(url, data=movie)
#print(p)

r = requests.get(url)
print(r.text)