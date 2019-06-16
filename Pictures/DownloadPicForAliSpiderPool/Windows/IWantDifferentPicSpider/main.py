# encoding: utf-8
import sys
sys.path.append('../')
from IWantDifferentPicSpider import picture_spider
from bs4 import BeautifulSoup

currentIndex = 1
#入口地址
url = 'https://www.woyaogexing.com/touxiang/index.html'

#设置爬取的网页数
maxIndex = 1

def loop(url):
    global currentIndex
    print('爬取网页：' + url)
    picture_spider.pic(url)
    currentIndex = (currentIndex + 1)
    url = 'https://www.woyaogexing.com/touxiang/index_%d.html' % currentIndex
    if currentIndex <= maxIndex:
        loop(url)
loop(url)
