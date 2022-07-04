from tmdbv3api import Movie
import requests
import json

movie_list = range(0, 500) # 20 movie_id per page
M_GENRES = [] # type = list
api = "https://api.themoviedb.org/3/movie/{movie_id}?api_key=adc8b11255c3f7d5434ddf79a9c2c670&language=en-US"

class Default(dict):
    def __missing__(self, key):
        return key

with open('ids.json', 'r') as f:
    loading = json.load(f)

for i in movie_list:
        url = api.format_map(Default(movie_id=loading[i].get("Movie_id")))
        r = requests.get(url)
        data = json.loads(r.text)

        tmp = data.get('genres')

        if data is not None:
            if tmp is not None:
                for j in range(len(tmp)):
                    tuple = {  # Dictionary Structure tmp
                        "Mid": data.get('id'),
                        "Genres": tmp[j]['name']
                    }
                    M_GENRES.append(tuple)

                    with open('M_GENRES.json', 'w') as f:
                        json.dump(M_GENRES, f)


        #print(movie_data)


