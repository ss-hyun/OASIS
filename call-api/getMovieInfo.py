from tmdbv3api import Movie
import requests
import json

movie_list = range(3000, 5000) # 20 movie_id per page
MOVIE = [] # type = list
overview = ""

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

            tuple = {  # Dictionary Structure tmp
                "Movie_id": data.get('id'),
                "Title": data.get('title'),
                "Release_date": date,
                "Running_time": data.get('runtime'),
                "Movie_rating": rate_str,  # Adult
                "Budget": data.get('budget'),
                "Image_link": data.get('poster_path'),
                "Overview": overview,
                "Total_revenue": data.get('revenue'),
                "Grade": data.get('vote_average'),
                "Vote_count": data.get('vote_count'),
            }
            MOVIE.append(tuple)

            # movie_data = json.dumps(tmp)

            with open('MOVIE3.json', 'w') as f:
                json.dump(MOVIE, f)

            # 0 ~ 2000: MOVIE1  2000~ 3000: MOVIE2  3000~5000: MOVIE3

