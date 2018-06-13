# -*- coding: utf-8 -*-
import urllib
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

def getBeautifulSoupObj(name):
    suffix = urllib.parse.quote(name) # 获取后缀
    html = urlopen("https://baike.baidu.com/item/" + suffix)
    bsObj = BeautifulSoup(html, "html5lib")
    return bsObj

def getBaikeText(name):
    '''接收中文姓名，返回对应百度百科的文字信息，若无则返回0'''
    bsObj = getBeautifulSoupObj(name)
    paragraph = bsObj.findAll("div", {"class": "para"})
    # paragraph = bsObj.findAll("div", text = "para")
    text = ""
    for i in range(len(paragraph)):
        text += paragraph[i].get_text()
    f = open(name + ".txt", 'w', encoding = "UTF-8")
    f.write(text)
    f.close()
    return text

def getBaikePhoto(name):
    '''接收中文姓名，返回对应百度百科的第一张图片'''
    bsObj = getBeautifulSoupObj(name)
    try:
        photourl = str(bsObj.find("div", {"class": "summary-pic"}).find("img")).split("\"")[1]
    except AttributeError:
        return None
    urlretrieve(photourl, name + ".jpg")

