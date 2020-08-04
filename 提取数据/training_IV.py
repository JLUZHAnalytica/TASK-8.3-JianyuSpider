from lxml.html import etree


def parse_buyer(html_code):
    data2 = etree.HTML(html_code)
    try:
        info_buyer = data2.xpath("//*[@class='cont-cont']/text()")[2]
    except:
        info_buyer = ''
    return info_buyer


def parse_winner(html_code):
    data2 = etree.HTML(html_code)
    try:
        info_buyer = data2.xpath("//*[@class='cont-cont']/text()")[6]
    except:
        info_buyer = ''
    return info_buyer


if __name__ == "__main__":
    import json
    parse_buyer()
    parse_winner()
