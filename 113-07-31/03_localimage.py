import requests

URL = 'https://notify-api.line.me/api/notify'
H, P, F= {}, {}, {}
H['Authorization'] = 'Bearer Jtd5DlFVD4kYq58F0m0ycM44EQmv00GDSfLRjs1QH5H'
P['message'] = '本機圖片'
#F['imageFile'] = open(r'C:\Users\m303\Pictures\star2.png','rb')
#F['imageFile'] = open('name.png','rb')
F['imageFile'] = open('./Pictures/name.png', 'rb')
requests.post(URL, headers=H, params=P,files=F)