# encoding: utf-8
'''
Created on 2015年5月29日

@author: ccb
'''
import sys
sys.path.append('..\\')
from KeywordsLongTail import Long_Tail_Keywords_Parser
from bs4 import BeautifulSoup

global currentPage

#设置爬取的最大网页数
pageCounts = 33

def loop(url):
    global currentPage
    currentPageUrl = url + '%d' %currentPage
    print('当前解析：' + currentPageUrl)
    Long_Tail_Keywords_Parser.keywords(currentPageUrl)

    currentPage = (currentPage + 1)

    if currentPage <= pageCounts:
       loop(url)

def str_to_hex(s):
    return ''.join([hex(ord(c)).replace('0x', '') for c in s])[::-1]

with open('keywords.txt', 'r') as f:
    for key in f.readlines():
        global currentPage
        keywrod = key.replace('\n', '')
        url = 'https://ci.5118.com/%s/?isPager=true&pageIndex=' %str_to_hex(keywrod)
        currentPage = 1
        loop(url)

