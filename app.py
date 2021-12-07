import os
import re
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restx import Resource, Api
from flask_mysqldb import MySQL
from dotenv import load_dotenv

app = Flask(__name__)
api = Api(app)
mysql = MySQL(app)

load_dotenv()

app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")

columns = []

@api.route('/admin')
class DoSimple(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM MOVIE")
        res = cur.fetchall()
        return jsonify(res)

    def post(self):
        #param = request.get_data()
        mid = request.form['Movie_id']
        title = request.form['Title']
        release = request.form['Release_date']
        run_time = request.form['Running_time']
        rating = request.form['Movie_rating']
        print(mid,title,release,run_time,rating)

        cur = mysql.connection.cursor()
        # f = open("/home/ss/record2.txt", 'w')
        # f.write('INSERT INTO MOVIE VALUES {} {} {} {} {} {} {} {} {} {}'.format(type(mid), mid, type(release), release, type(title), title, type(run_time), run_time, type(rating), rating ))
        # f.close()
        input = "INSERT INTO MOVIE(Movie_id,Release_date,Title,Running_time,Movie_rating) VALUES ({},{},{},{},{})".format(mid, release, title, run_time, rating)
        ret = cur.execute(input)

        mysql.connection.commit()

        cur.close()
        if ret :
            return 'success'
        else:
            return 'fail'


if __name__ == '__main__':
    app.run(debug=True)
    cur = mysql.connection.cursor()
    cur.execute("SHOW FULL COLUMNS FROM MOVIE")
    columns.append(cur.fetchall())
    print(columns)

