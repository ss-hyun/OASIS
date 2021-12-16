from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
import requests
import json

host = 'http://127.0.0.1:5000/'

path = 'movie'
url = host + path


main = Blueprint('main', __name__, url_prefix='/')

@main.route('/main', methods=['GET'])
def index():
    name = "/popular_movie"
    r = requests.get(url+name, params={ 'page': 1 })
    movie = json.loads(r.text)

    return render_template('/main/index.html', movie=movie)

@main.route('/movie', methods=['GET'])
def movie():
    page = int(request.args['page'])
    order = int(request.args['order'])
    if order == 0:
        name = "/popular_movie"
        order = "Popular"
    elif order == 1:  
        name = "/higher_grade"
        order = "Grade"
    elif order == 2:  
        name = "/up_comming"
        order = "UP Comming"
    r = requests.get(url+name, params={ 'page': page })
    movie = json.loads(r.text)

    return render_template('/main/movie.html', movie=movie, order=order)

@main.route('/search', methods=['GET'])
def search():
    testData = 'testData array'
    return render_template('/main/search.html', testDataHtml=testData)

@main.route('/movie_deep', methods=['GET'])
def movie_deep():
    mvid = int(request.args['mvid'])
    name = "/movie_deep"
    r = requests.get(url+name, params={ 'mvid': mvid })
    movie = json.loads(r.text)
    g_movie = json.loads(movie['Genres_popular']) if movie['Genres_popular'] else []
    while len(g_movie) < 5: g_movie.append(None)
    participate = json.loads(movie['Officials_thin']) if movie['Officials_thin'] else []
    while len(participate) < 5: participate.append(None)
    movie = movie['movie_info']

    return render_template('/main/movie_deep.html', movie=movie, g_mv=g_movie, participate=participate)

@main.route('/participate_deep', methods=['GET'])
def participate_deep():
    moid = int(request.args['moid'])
    name = "/participate_deep"
    r = requests.get(url+name, params={ 'moid': moid })
    official = json.loads(r.text)
    print(official['participate_in'])
    participate_mv = json.loads(official['participate_in']) if official['participate_in'] else []
    while len(participate_mv) < 5: participate_mv.append(None)

    return render_template('/main/participate_deep.html', official=official, par_mv=participate_mv)