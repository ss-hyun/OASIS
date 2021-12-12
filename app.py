import os
import json
from flask import Flask, jsonify, request
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

@api.route('/movie/<string:name>')
class DoSimple(Resource):
    def get(self, name):
        if name == "up_comming":
            pg = int(request.args['page'])
            cur = mysql.connection.cursor()
            par = { "req" : name }
            cur.callproc('Get_mv_thin',(pg, json.dumps(par), ""))
            cur.execute('SELECT @_Get_mv_thin_2')
            res = cur.fetchall()
            return jsonify(res[0][0])

        if name == "popular_movie":
            pg = int(request.args['page'])
            cur = mysql.connection.cursor()
            par = { "req" : name }
            cur.callproc('Get_mv_thin',(pg, json.dumps(par), ""))
            cur.execute('SELECT @_Get_mv_thin_2')
            res = cur.fetchall()
            return jsonify(res[0][0])

        if name == "higher_grade":
            pg = int(request.args['page'])
            cur = mysql.connection.cursor()
            par = { "req" : name }
            cur.callproc('Get_mv_thin',(pg, json.dumps(par), ""))
            cur.execute('SELECT @_Get_mv_thin_2')
            res = cur.fetchall()
            return jsonify(res[0][0])

        if name == "participate_officials":
            pg = int(request.args['page'])
            moid = int(request.args['moid'])
            cur = mysql.connection.cursor()
            par = { "req" : name, "oid" : moid }
            cur.callproc('Get_mv_thin',(pg, json.dumps(par), ""))
            cur.execute('SELECT @_Get_mv_thin_2')
            res = cur.fetchall()
            return jsonify(res[0][0])

        if name == "movie_deep":
            mvid = int(request.args['mvid'])
            cur = mysql.connection.cursor()
            cur.callproc('Get_mv_deep',(mvid, '{"req":""}', ""))
            cur.execute('SELECT @_Get_mv_deep_2')
            res = cur.fetchall()
            return jsonify(res[0][0])
        
        if name == "participated_movie":
            pg = int(request.args['page'])
            mvid = int(request.args['mvid'])
            cur = mysql.connection.cursor()
            par = { "req" : name, "mid" : mvid }
            cur.callproc('Get_mo_thin',(pg, json.dumps(par), ""))
            cur.execute('SELECT @_Get_mo_thin_2')
            res = cur.fetchall()
            return jsonify(res[0][0])

        if name == "participate_deep":
            moid = int(request.args['moid'])
            cur = mysql.connection.cursor()
            cur.callproc('Get_mo_deep',(moid, '{"req":""}', ""))
            cur.execute('SELECT @_Get_mo_deep_2')
            res = cur.fetchall()
            return jsonify(res[0][0])

        if name == "search_movie_name":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM MOVIE;")
            res = cur.fetchall()
            return jsonify(res)

        if name == "search_person_name":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM MOVIE;")
            res = cur.fetchall()
            return jsonify(res)


@api.route('/admin/<string:name>')
class DoSimple(Resource):
    def get(self, name):
        if name == "movie":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM MOVIE;")
            res = cur.fetchall()
            return jsonify(res)

    def post(self, name):
        if name == "genres":
            data_path = request.get_data().decode()

            data = []

            with open(data_path, encoding='utf-8') as f:
                pass
                
            print(len(data))
            
            ret = []
            
            cur = mysql.connection.cursor()
            for d in data:
                input = "SELECT * FROM M_GENRES WHERE Mid={} AND Genres='{}';".format(d["Mid"], d["Genres"])
                cur.execute(input)
                if not cur.fetchall():
                    input = 'CALL Gr_insert (\'{}\');'.format(json.dumps(d))
                    if cur.execute(input): ret.append(d)
                    mysql.connection.commit()
                
            f.close()

            with open('insert+fail({}).json'.format(data_path.split("/")[4].split('.')[0]),'w', encoding='utf-8') as make_file:
                json.dump(ret, make_file, indent="\t")
            
            make_file.close()
            cur.close()
        elif name == "movie":
            
            data_path = request.get_data().decode()
            
            with open(data_path, encoding='utf-8') as f:
                data = json.load(f)
            print(len(data))
            
            ret = []
            cur = mysql.connection.cursor()
            id=[]

            for d in data:
                # input = "SELECT * FROM MOVIE WHERE Movie_id={};".format(d["Movie_id"])
                d["Title"] = '{}'.format(d["Title"]).replace("'","''")
                d["Title"] = '{}'.format(d["Title"]).replace("\r"," ")
                d["Title"] = '{}'.format(d["Title"]).replace("\n"," ")
                d["Title"] = '{}'.format(d["Title"]).replace("\t"," ")
                d["Title"] = '{}'.format(d["Title"]).replace("\\","\\\\")
                d["Title"] = '{}'.format(d["Title"]).replace("\"","\\\"")
                d["Overview"] = '{}'.format(d["Overview"]).replace("'","''")
                d["Overview"] = '{}'.format(d["Overview"]).replace("\r"," ")
                d["Overview"] = '{}'.format(d["Overview"]).replace("\n"," ")
                d["Overview"] = '{}'.format(d["Overview"]).replace("\t"," ")
                d["Overview"] = '{}'.format(d["Overview"]).replace("\\","\\\\")
                d["Overview"] = '{}'.format(d["Overview"]).replace("\"","\\\"")
                if d["Release_date"] == "": d["Release_date"] = None
                # cur.execute(input)
                # s=cur.fetchall()
                # if not s:
                input = 'CALL Mv_insert_or_update (\'{}\');'.format(json.dumps(d))
                if cur.execute(input): ret.append(d)
                mysql.connection.commit()
                
            with open('insert+fail({}).json'.format(data_path.split("/")[4].split('.')[0]),'w', encoding='utf-8') as make_file:
                json.dump(ret, make_file, indent="\t")
            
            make_file.close()

            f.close()
                
            cur.close()

        elif name == "movie_officials":
            data_path = request.get_data().decode()
            with open(data_path, encoding='utf-8') as f:
                data = json.load(f)
            print(len(data["movie"]))
            
            ret = []
            cur = mysql.connection.cursor()

            for d in data["movie"]:
                # input = "SELECT * FROM MOVIE_OFFICIALS WHERE Officials_id={};".format(d["Officials_id"])
                d["Name"] = '{}'.format(d["Name"]).replace("'","''")
                d["Name"] = '{}'.format(d["Name"]).replace("\r"," ")
                d["Name"] = '{}'.format(d["Name"]).replace("\n"," ")
                d["Name"] = '{}'.format(d["Name"]).replace("\t"," ")
                d["Name"] = '{}'.format(d["Name"]).replace("\\","\\\\")
                d["Name"] = '{}'.format(d["Name"]).replace("\"","\\\"")
                d["Biography"] = '{}'.format(d["Biography"]).replace("'","''")
                d["Biography"] = '{}'.format(d["Biography"]).replace("\r"," ")
                d["Biography"] = '{}'.format(d["Biography"]).replace("\n"," ")
                d["Biography"] = '{}'.format(d["Biography"]).replace("\t"," ")
                d["Biography"] = '{}'.format(d["Biography"]).replace("\\","\\\\")
                d["Biography"] = '{}'.format(d["Biography"]).replace("\"","\\\"")
                # cur.execute(input)
                # if not cur.fetchall():
                input = 'CALL Mo_insert_or_update (\'{}\');'.format(json.dumps(d))
                if cur.execute(input):  ret.append(d)
                mysql.connection.commit()
                
                
            with open('insert+fail({}).json'.format(data_path.split("/")[4].split('.')[0]),'w', encoding='utf-8') as make_file:
                json.dump(ret, make_file, indent="\t")
            
            make_file.close()
                
            cur.close()

        elif name == "act_in":
            data_path = request.get_data().decode()
            with open(data_path, encoding='utf-8') as f:
                data = json.load(f)
            print(len(data["movie"]))
            
            ret = []
            cur = mysql.connection.cursor()

            for d in data["movie"]:
                input = "SELECT * FROM ACT_IN WHERE Mid={} and Oid={};".format(d["Mid"], d["Oid"])
                cur.execute(input)
                if not cur.fetchall():
                    input = 'CALL Act_insert (\'{}\');'.format(json.dumps(d))
                    if cur.execute(input):  ret.append(d)
                mysql.connection.commit()
                
                
            with open('insert+fail({}).json'.format(data_path.split("/")[4].split('.')[0]),'w', encoding='utf-8') as make_file:
                json.dump(ret, make_file, indent="\t")
            
            make_file.close()

            f.close()
                
            cur.close()

        elif name == "directed":
            data_path = request.get_data().decode()
            with open(data_path, encoding='utf-8') as f:
                data = json.load(f)
            print(len(data["movie"]))
            
            ret = []
            cur = mysql.connection.cursor()

            for d in data["movie"]:
                input = "SELECT * FROM DIRECTED WHERE Mid={} and Oid={};".format(d["Mid"], d["Oid"])
                cur.execute(input)
                if not cur.fetchall():
                    input = 'CALL Direc_insert (\'{}\');'.format(json.dumps(d))
                    if cur.execute(input):  ret.append(d)
                mysql.connection.commit()
                
                
            with open('insert+fail({}).json'.format(data_path.split("/")[4].split('.')[0]),'w', encoding='utf-8') as make_file:
                json.dump(ret, make_file, indent="\t")
            
            make_file.close()

            f.close()
                
            cur.close()

        if ret :
            return 'success'
        else:
            return 'fail'


if __name__ == '__main__':
    app.run(debug=True)

