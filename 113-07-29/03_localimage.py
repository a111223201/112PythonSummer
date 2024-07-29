import requests

URL = 'https://notify-api.line.me/api/notify'
H, P, F= {}, {}, {}
H['Authorization'] = 'Bearer Jtd5DlFVD4kYq58F0m0ycM44EQmv00GDSfLRjs1QH5H'
P['message'] = '本機圖片'
F['imageFile'] = open('name.jpg','rb')
requests.post(URL, headers=H, params=P)

