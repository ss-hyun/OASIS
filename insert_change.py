import requests
import sys
import schedule
from datetime import datetime
import json
import time

host = 'http://127.0.0.1:5000/'

path = 'admin'
url = host + path
name = "/change"

def rooping():
    filename = datetime.today().strftime('%Y%m%d') + ".json"

    p = requests.post(url + name, data="/home/ss/MEI_database/{}".format(filename))
    print(p)

'''schedule.every().days.at("11:40").do(rooping)

while True:
    schedule.run_pending()
    time.sleep(1)'''