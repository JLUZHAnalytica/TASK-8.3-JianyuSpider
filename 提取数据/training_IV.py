import json
from lxml.html import etree
import urllib.request as r
def parse_buyer():
    i=0
    with open("html_list.json","r",encoding="utf-8") as f:
        data=json.load(f)
        c=open("cre.html","w+",encoding="utf-8")
        html=data[0]["html_code"]
        c.write(html)
        response=r.Request(url='file:///D:/DLR/dlr-workplace/project/VII/cre.html')
        data1=r.urlopen(response).read().decode("utf-8")
        data2=etree.HTML(data1)
        try:
            info_buyer=data2.xpath("//*[@class='cont-cont']/text()")[2]
        except:
            info_buyer=''
        print(info_buyer)
        i=i+1

def parse_winner():
    j=0
    with open("html_list.json","r",encoding="utf-8") as f:
        data=json.load(f)
        c=open("cre.html","w+",encoding="utf-8")
        html=data[0]["html_code"]
        c.write(html)
        response=r.Request(url='file:///D:/DLR/dlr-workplace/project/VII/cre.html')
        data1=r.urlopen(response).read().decode("utf-8")
        data2=etree.HTML(data1)
        try:
            info_buyer=data2.xpath("//*[@class='cont-cont']/text()")[6]
        except:
            info_buyer=''
        print(info_buyer)
        j=j+1
parse_buyer()
parse_winner()
