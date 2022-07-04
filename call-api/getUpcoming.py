from tmdbv3api import Movie
import requests
import json

page_range = range(1, 12) # 20 movie_id per page
movie_list = range(0, 20)
upmovie_ids = [] # type = list
api = "https://api.themoviedb.org/3/movie/upcoming?api_key=adc8b11255c3f7d5434ddf79a9c2c670&language=en-US&page={page}"

class Default(dict):
    def __missing__(self, key):
        return key

for name in page_range:
    url = api.format_map(Default(page=name))
    r = requests.get(url)
    info = json.loads(r.text)

    #print(info)
    data = info.get("results")
    #print(data)

    for movie in movie_list:

        rate = data[movie].get('adult')
        if rate:
            rate_str = "adult"
        else:
            rate_str = "normal"

        upmovie_ids.append({
            "Movie_id": data[movie].get("id"),  # "list" type: dictionary
            "Title": data[movie].get('title'),
            "Release_date": data[movie].get('release_date'),
            # "Running_time": data.get('runtime'),
            "Movie_rating": rate_str,  # Adult
            # "Budget": data.get('budget'),
            "Image_link": data[movie].get('poster_path'),
            "Overview": data[movie].get('overview'),
            # "Total_revenue": data.get('revenue'),
            "Grade": data[movie].get('vote_average'),
            "Vote_count": data[movie].get('vote_count'),
        })


    '''for list in data.get("results"):

        rate = data.get('adult')
        if rate:
            rate_str = "adult"
        else:
            rate_str = "normal"

        upmovie_ids.append({
            "Movie_id":list.get("id"), # "list" type: dictionary
            "Title": data.get('title'),
            "Release_date": data.get('release_date'),
            #"Running_time": data.get('runtime'),
            "Movie_rating": rate_str,  # Adult
            #"Budget": data.get('budget'),
            "Image_link": data.get('poster_path'),
            "Overview": data.get('overview'),
            #"Total_revenue": data.get('revenue'),
            "Grade": data.get('vote_average'),
            "Vote_count": data.get('vote_count'),
        })'''

#json 파일로 저장
with open('upcoming_ids.json','w') as f:
    json.dump(upmovie_ids, f)

#json 파일 불러오기
#with open('ids.json','r') as f:
    #loading=json.load(f)


