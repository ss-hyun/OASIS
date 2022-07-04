from tmdbv3api import Movie
from datetime import datetime
import time
import schedule
import requests
import json
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

movie_list = range(0, 100) # 20 movie_id per page
MOVIE = [] # type = list
GENRE = []
ACTIN = []
DIRECTED = []

api = "https://api.themoviedb.org/3/movie/{movie_id}?api_key=adc8b11255c3f7d5434ddf79a9c2c670&language=en-US"
api2 = "https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=adc8b11255c3f7d5434ddf79a9c2c670"
apikey="adc8b11255c3f7d5434ddf79a9c2c670"

class Default(dict):
    def __missing__(self, key):
        return key

headers = requests.utils.default_headers()
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

def rooping():

    with open('/home/ss/change_ids.json', 'r') as f:
        loading = json.load(f)

    filename = datetime.today().strftime('%Y%m%d') + ".json"
    #print(filename)

    for i in movie_list:
        url = api.format_map(Default(movie_id=loading[i].get("Movie_id")))
        r = requests.get(url)
        data = json.loads(r.text)

        url2 = api2.format_map(Default(movie_id=loading[i].get("Movie_id")))
        r2 = requests.get(url2, verify=False)
        data2 = json.loads(r2.text)

        if data.get('id') is not None:
            if data.get('release_date') is not None:
                date = data.get('release_date')
                date = date.replace('-', '')
            else:
                date = data.get('release_date')

            rate = data.get('adult')
            if rate:
                rate_str = "adult"
            else:
                rate_str = "normal"

            if data.get('overview') is not None:
                if len(data.get("overview")) >= 490:
                    overview = data.get("overview")
                    overview = overview[:490] + "..."
                else:
                    overview = data.get('overview')

            movie_id = data.get('id')
            tmp = data.get('genres')

            GENRE = []
            ACTIN = []
            DIRECTED = []

            if tmp:
                for j in range(len(tmp)):
                    genre = {  # Dictionary Structure tmp
                        "Mid": movie_id,
                        "Genres": tmp[j]['name']
                    }
                    GENRE.append(genre)

            if (data2 is not None):
                if (data2.get("cast") is not None):
                    for list in data2.get("cast"):
                        if (list is not None):
                            cast_api = "https://api.themoviedb.org/3/person/{person_id}?api_key=adc8b11255c3f7d5434ddf79a9c2c670"
                            url_cast = cast_api.format_map(Default(person_id=list.get("id")))
                            cast_r = requests.get(url_cast, verify=False)
                            cast_data = json.loads(cast_r.text)
                            act_in = {
                                "Mid": movie_id,
                                "Oid": list.get("id")
                            }
                            # print(act_in)
                            ACTIN.append(act_in)

            if data2.get("cast") is not None and data2 is not None:
                for list in data2.get("crew"):
                    if list is not None and list.get("job") == "Director":
                        if list.get("id") is not None:
                            crew_api = "https://api.themoviedb.org/3/person/{person_id}?api_key=adc8b11255c3f7d5434ddf79a9c2c670"
                            url_cast = crew_api.format_map(Default(person_id=list.get("id")))
                            cast_r = requests.get(url_cast, verify=False)
                            cast_data = json.loads(cast_r.text)
                            directed = {
                                "Mid": movie_id,
                                "Oid": list.get("id")
                            }
                            # print(directed)
                            DIRECTED.append(directed)

            tuple = {
                "movie": {
                    "Movie_id": movie_id,
                    "Title": data.get('title'),
                    "Release_date": date,
                    "Running_time": data.get('runtime'),
                    "Movie_rating": rate_str,  # Adult
                    "Budget": data.get('budget'),
                    "Image_link": data.get('poster_path'),
                    "Overview": overview,
                    "Total_revenue": data.get('revenue'),
                    "Grade": data.get('vote_average'),
                    "Vote_count": data.get('vote_count')
                },
                "Genre": GENRE,
                "ACT_IN": ACTIN,
                "DIRECTED": DIRECTED
            }
            MOVIE.append(tuple)

            with open('/home/ss/MEI_database/{}'.format(filename), 'w') as f:
                json.dump(MOVIE, f)
rooping()
#schedule.every().days.at("01:50").do(rooping)

#while True:
#    schedule.run_pending()
#    time.sleep(1) 