# encoding: utf-8
'''
Created on 2015年5月29日

@author: ccb
'''
import sys
sys.path.append('..\\')
from py import spyder_for_pic
from bs4 import BeautifulSoup
from collections import deque

queue = deque()
urlcont = 1
#入口地址
#url = 'http://www.wmpic.me/tupian/yijing/'
url = 'http://www.qqjia.com/face/nvshengtouxiang%d.htm' %urlcont
queue.append(url)
count1 = 0
#设置爬取的网页数
url_cont = 48

def loop(url):
    global urlcont
    print('爬取网页：' + url)
    spyder_for_pic.pic(url)
    urlcont = (urlcont + 1)
    url = 'http://www.qqjia.com/face/nvshengtouxiang%d.htm' % urlcont
    if urlcont <= url_cont:
        loop(url)
loop(url)