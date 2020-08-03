import re


def parse(text):
    bidtime_place = []
    bidtime_list = re.findall(r"[0-9]+年[0-9]+月[0-9]+日\s*.*分", text)
    if len(bidtime_list) == 0:
        return
    for m in re.finditer(r"[0-9]+年[0-9]+月[0-9]+日\s*.*分", text):
        bidtime_place.append(m.span()[0])
    title_place = re.search(r"开标时间", text).span()[0]
    if title_place == None:
        return bidtime_list[0]
    min_dis = 9999999999
    min_index = -1
    i = 0
    for p in bidtime_place:
        if abs(title_place-p) < min_dis:
            min_dis = abs(title_place-p)
            min_index = i
            i += 1
    return bidtime_list[min_index]


if __name__ == "__main__":
    print(parse("""
法人代表授权委托书原件，招标文件售后不退
售价：￥300.0 元，本公告包含的招标文件售价总和
四、提交投标文件截止时间、开标时间和地点
2020年08月25日 09点30分（北京时间）（自招标文件开始发出之日起至投标人提交投标文件截止之日止，不得少于20日）
地点：北京市西城区广安门外大街248号机械大厦618会议室
五、公告期限
        """))
