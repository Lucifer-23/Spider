# encoding: utf-8
import sys
sys.path.append('../')
from PictureSpider import picture_spider
from bs4 import BeautifulSoup
from collections import deque

queue = deque()
currentIndex = 1
#入口地址
#url = 'http://www.wmpic.me/tupian/yijing/'
url = 'http://www.qqjia.com/face/nanshengtouxiang%d.htm' % currentIndex
queue.append(url)
count1 = 0
#设置爬取的网页数
url_cont = 40

def loop(url):
    global currentIndex
    print('爬取网页：' + url)
    picture_spider.pic(url)
    urlcont = (urlcont + 1)
    url = 'http://www.qqjia.com/face/nvshengtouxiang%d.htm' % urlcont
    if urlcont <= url_cont:
        loop(url)
loop(url)
