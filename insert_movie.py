import requests
import json
import time

host = 'http://127.0.0.1:5000/'

path = 'admin'
url = host + path
name = "/movie"

# with open('/home/ss/MEI_database/MOVIE1.json', encoding='utf-8') as f:
#     mv_list = json.load(f)

# param = { 'mv' : str(mv_list).encode('utf-8') }
p = requests.post(url+name, data="/home/ss/MEI_database/MOVIE1.json")
print(p)
p = requests.post(url+name, data="/home/ss/MEI_database/MOVIE2.json")
print(p)

# ls = []
# i = 0
# for mv in mv_list:
#     p = requests.post(url+name, data=str(mv).encode("utf-8"))
#     print(p)
#     if p.status_code == 500:
#         ls.append(mv)
#     time.sleep(0.1)
#     i += 1
#     if i>100: break

# print(ls)