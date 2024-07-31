import requests


IMG = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTufxiYTNhHz87MO9sDuUpeAbChn6oPDAv5VA&s'
URL = 'https://notify-api.line.me/api/notify'
H, P, F= {}, {}, {}
H['Authorization'] = 'Bearer qWbmPi4kyFEP6TEugqccIPIv9pr2ofbuRZOYazBWqZQ'
P['message'] = '群組網路圖片'
F['imageFile'] = requests.get(IMG).content
requests.post(URL, headers=H, params=P,files=F)