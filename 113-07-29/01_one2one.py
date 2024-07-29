import requests

URL = 'https://notify-api.line.me/api/notify'
H, P = {}, {}
H['Authorization'] = 'Bearer Jtd5DlFVD4kYq58F0m0ycM44EQmv00GDSfLRjs1QH5H'
P['message'] = '今天是星期一'
requests.post(URL, headers=H, params=P)