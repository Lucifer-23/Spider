# encoding: utf-8
'''
Created on 2015年5月29日

@author: ccb
'''
import sys
sys.path.append('..\\')
from BaiDuTop import BaiDuTopParser
from bs4 import BeautifulSoup

currentIndex = 1

#入口地址
url = 'http://top.baidu.com/buzz?b=%d' %currentIndex

#设置爬取的最大S索引数
maxIndex = 500

def loop(url):
    global currentIndex
    print('当前解析：' + url)
    BaiDuTopParser.top(url)

    currentIndex = (currentIndex + 1)
    url = 'http://top.baidu.com/buzz?b=%d' % currentIndex
    if currentIndex <= maxIndex:
       loop(url)

loop(url)

