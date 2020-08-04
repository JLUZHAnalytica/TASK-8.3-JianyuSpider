import json
from zyf import parse_bidtime
import time


def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    # 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    return dt


with open("data/result_half.json", 'r') as fd:
    data = json.load(fd)

for item in data:
    item["publishtime"] = timestamp_datetime(item["publishtime"])
    item.update({"buyer": parse_buyer(item["html_code"])})
    item.update({"winner": parse_winner(item["html_code"])})
    item.update({"bidtime": parse_bidtime(item["html_code"])})

with open("data/result_final.json", 'w') as fd:
    fd.write(json.dumps(data, ensure_ascii=False, indent=4))
