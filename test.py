import json

def read_file(file_path):
    data = []
    with open(file_path, encoding='utf-8') as f:
        str = f.read()
        d = ''
        i = 0
        left = 0
        while i < len(str):
            d += str[i]
            if d[-1] == '{':
                left += 1
                if left == 1:
                    d = '{'

            elif d[-1] == '}':
                left -= 1
                if left == 0:
                    jd = json.loads(d)
                    if jd["Movie_id"]==754: print(jd)
                    data.append(jd)

            i += 1

    return data

data = read_file('/home/ss/MEI_database/MOVIE2.json')
#print(data)
print(len(data))