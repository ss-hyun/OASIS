import requests

host = 'http://127.0.0.1:5000/'

path = 'admin'
url = host + path
name = "/movie"

r = requests.get(url+name)
print(r.text)

movie = { 'Movie_id': 10, 
            'Title':'"apitest3"', 
            'Release_date': 19970926, 
            'Running_time':136, 
            'Movie_rating':'"12"' ,
            "Budget" : 1234,
            "Image_link" : '"/test/api"',
            "Overview" : '"hahaha"', 
            "Total_revenue" : 12344, 
            "Grade" : 10.1, 
            "Vote_count" : 10
}


p = requests.post(url+name, data=movie)
print(p)

r = requests.get(url+name)
print(r.text)