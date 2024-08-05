import requests

URL ='https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {}
P['Authorization'] = 'CWA-1DC7471C-30C9-4497-9682-451134DF031E'
r = requests.get(URL,params=P)
t = r.json()

n = len(t['records']['Station'])
for i in range(n):
    print(i,t['records']['Station'][i]['StationName'])