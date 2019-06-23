# encoding: utf-8

import sys
import re
sys.path.append('../')
from Linux import Website_Keywords_Parser
from bs4 import BeautifulSoup

global currentIndex

#设置爬取的最大网页数
pageCounts = 24

def loop(url, resultFile):
    global currentIndex
    currentPageUrl = url + '%d' %currentIndex
    print('当前解析：' + currentPageUrl)
    Website_Keywords_Parser.keywords(currentPageUrl,resultFile)

    currentIndex = (currentIndex + 1)

    if currentIndex <= pageCounts:
       loop(url,resultFile)

with open('website.txt', 'r') as f:
    for website in f.readlines():
        global currentIndex
        site = website.replace('\n', '')
        url = 'http://www.ciku5.com/s?wd=%s&citype=1&sort=0&p=' %site
        currentIndex = 1
        pattern = re.compile('www.|.com|.net|.cn', re.I)
        loop(url, pattern.sub('', site))

