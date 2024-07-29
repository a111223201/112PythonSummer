import requests

URL = 'https://notify-api.line.me/api/notify'
H, P = {}, {}
H['Authorization'] = 'Bearer Jtd5DlFVD4kYq58F0m0ycM44EQmv00GDSfLRjs1QH5H'
P['message'] = '貼圖測試'
P['stickerPackageId'] = 6325
P['stickerId']=10979907
requests.post(URL, headers=H, params=P)

