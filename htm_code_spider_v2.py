# 这个爬虫是为了解决第一次爬取时有一些页面爆出验证的问题

import json
import requests
import time

with open("data/html_list_half.json", 'r') as fd:
    data = json.load(fd)

headers = {
    'cookie': 'SESSIONID=8224ced3a6502d627bb97ecfeabb8d79343c183d; SESSIONID=8224ced3a6502d627bb97ecfeabb8d79343c183d; userid_secure=RIQcgdRiKLvx4QboUN6JN6I36p68Zn9ymgokQy3zr/UvnUapfFllxb2a91AgpH9crUvaHQgCNx+5tz8fkaLuuxphoUx2eux+LVmlGv3D2LB3dje76ZUq6O12s9lvIGYs85DuPs/cszjc2/y6Kx3TUbwENsIxm691wR08kEROnwB4z+/zO5ClpYK7XP5/LJYeF099za9m7/JT8C/CZY4gi0Bv6dQWbIDNSY0I+6IANRIJB3yoZo41vQz11vuyRRalV1/cbgnCvU8Gfd/mav524wihuIveUR643Z2rwsgL9Vn13lc0p9bcWWTuRGaWrdh1XDSJZ/y6rQ2oSqG4MGCAtSoqKjIwMjAtMDgtMDIgMDA6MDA6MDA=',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
need_cnt = 0
total_cnt = 0
err_cnt = 0


def scrape(url):
    response = requests.get(url, headers=headers)
    time.sleep(3)
    return response.text


for item in data:
    total_cnt += 1
    if item["html_code"][5:15] == "antiVerify":
        need_cnt += 1
        item["html_code"] = scrape(item["url"])
        if item["html_code"][5:15] == "antiVerify":
            input("请打开网页手动填验证码，然后按回车继续")
            item["html_code"] = scrape(item["url"])
        print(f"当前完成{total_cnt/len(data)*100}%\n已处理{need_cnt}个")

with open("data/html_list_half.json", 'w') as fd:
    fd.write(json.dumps(data, ensure_ascii=False, indent=4))
