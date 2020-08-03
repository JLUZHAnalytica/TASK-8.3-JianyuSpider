import re


def parse(text):
    bidtime_place = []
    bidtime_list = re.findall(r"([0-9]+年[0-9]+月[0-9]+日\s*.*?)[(（]*北京", text)
    if len(bidtime_list) == 0:
        return
    for m in re.finditer(r"([0-9]+年[0-9]+月[0-9]+日\s*.*?)[(（]*北京", text):
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
    with open("data/demo_text.txt", 'r') as fd:
        text = fd.read()
    print(parse(text))
