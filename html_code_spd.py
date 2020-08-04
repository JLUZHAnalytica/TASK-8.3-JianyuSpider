import json
import time

import requests

headers = {
    'cookie': '',
    'user-agent': ''
}
with open('brief_list.json', 'r', encoding="utf-8") as load_f:
    data = json.load(load_f)

for i in range(500):
    xid = data[i]['_id']
    data[i].clear()
    data[i] = {'_id': xid}
    gonzo = {"url": "https://www.jianyu360.com/article/content/" + xid + '.html'}
    data[i].update(gonzo)
    url = data[i]['url']
    response = requests.get(url, headers=headers)
    hcom = {"html_code": response.text}
    data[i].update(hcom)
    time.sleep(10)
with open('html_list.json', 'w', encoding='utf-8') as f:
    data_col = json.dumps(data, ensure_ascii=False)
    f.write(data_col)
