from tmdbv3api import Movie
import schedule
import requests
import json
import time
import datetime
import sys

page_range = range(1, 2) # 20 movie_id per page
movie_list = range(0, 100)
change_ids = [] # type = list

api = "https://api.themoviedb.org/3/movie/changes?api_key=adc8b11255c3f7d5434ddf79a9c2c670&language=en-US&page={page}"

class Default(dict):
    def __missing__(self, key):
        return key

def rooping():
    for name in page_range:
        url = api.format_map(Default(page=name))
        r = requests.get(url)
        info = json.loads(r.text)
        data = info.get("results")
        for movie in movie_list:
            change_ids.append({
                "Movie_id": data[movie].get("id"),  # "list" type: dictionary
            })
    #json 파일로 저장
    with open('/home/ss/change_ids.json','w') as f: 
        json.dump(change_ids, f)

schedule.every().days.at("01:40").do(rooping)

while True:
    schedule.run_pending()
    time.sleep(1)
