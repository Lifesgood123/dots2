from urllib.request import urlopen as ureq
import json

def get_json(local):
    f = ureq('http://api.wunderground.com/api/0bf213c89d5d826c/geolookup/conditions/q/IA/'+local+'.json')
    data = json.loads(f.read())
    return data

f = get_json('Winston-Salem')

key_list = list(f.keys)
for i in key_list:
    print(i)
    for j in list(f[i]):
        print(j)
        print(f[i][j])


