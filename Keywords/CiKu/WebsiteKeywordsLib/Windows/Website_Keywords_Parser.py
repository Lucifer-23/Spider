import urllib
import urllib.request

import time 
import random 
from bs4 import BeautifulSoup
import requests,os
def user_agent(url):
    req_timeout = 30
    req = urllib.request.Request(url,headers = {
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Cookie': 'UM_distinctid=16b5b4d155b542-0e357974abd5c5-e353165-144000-16b5b4d155c307; Hm_lvt_5e1b2743b16ff0ee74bb0c0abf56edc9=1560604909; bdshare_firstime=1560604909474; user_login_id=obt2dKOvTlMWQaAsL8Hqq%2bYbImzPxXqSRW8O2uFQVx0uOpZ6gOLmdw%3d%3d; ASP.NET_SessionId=44cje1pq2ez5f1pcjx0jidtr; CNZZDATA5581059=cnzz_eid%3D1245288355-1560604514-%26ntime%3D1560664812'
    })
    page = urllib.request.urlopen(req,None,req_timeout)
    html = page.read()
    print('爬取网页 “' + url + '” 成功')
    return html 

def keywords(url, resultFile):
    soup = BeautifulSoup(user_agent(url),'html.parser')
    allKeywords = soup.find_all(['a'])
    print('解析网页 “' + url + '” 成功')
    for item in allKeywords:
        classLabel = item.get('class')
        hrefLabel = item.get('href')

        if not classLabel:
            continue
        if 'link' not in classLabel:
            continue
        if 'blue' not in classLabel:
            continue
        if not hrefLabel.startswith('/s?wd='):
            continue
        keyword = item.string
        print('获取网站关键词 “' + keyword + '” 成功')
        fp = open(".\\Results\\%s.txt" %resultFile, "a", encoding="utf-8")
        fp.write(keyword)
        fp.write(u"\n")
        fp.close()
