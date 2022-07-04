from tmdbv3api import Movie
import requests
import json

page_range = range(1, 139) #페이지 1~500까지
api = "https://api.themoviedb.org/3/movie/now_playing?api_key=adc8b11255c3f7d5434ddf79a9c2c670&language=en-US&page={page}"

class Default(dict):
    def __missing__(self, key):
        return key
movie_ids=[]

for name in page_range:
    url = api.format_map(Default(page=name))
    r = requests.get(url)
    data = json.loads(r.text)
    for list in data.get("results"):
        movie_ids.append({
            "Movie_id":list.get("id")
        })
#json 파일로 저장
print(movie_ids)
with open('now_playing.json','w') as f: 
    json.dump(movie_ids,f)
#json 파일 불러오기
#with open('ids.json','r') as f:
#    loading=json.load(f,encoding='cp949')

