# -*- coding: utf-8 -*
import urllib
import urllib.request

import time 
import random 
from bs4 import BeautifulSoup
import requests,os
def user_agent(url):
    req_timeout = 30
    req = urllib.request.Request(url,headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    page = urllib.request.urlopen(req,None,req_timeout)
    html = page.read()
    print('爬取网页 “' + url + '” 成功')
    return html 
def pic(url):
    soup = BeautifulSoup(user_agent(url),'html.parser')
    img = soup.find_all(['img'])
    print('解析网页 “' + url + '” 成功')
    for pic in img:
        link = pic.get('src')

        print('获取图片 “' + link + '” 成功')

        if link is None:
            continue
        if  link[-3:] in ['gif']:
            continue
        try: 
            #读取图片到content
            response = requests.get('https:' + link,headers = {
                                                   'Pragma': 'no-cache',
                                                   'Accept-Encoding': 'gzip, deflate',
                                                   'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
                                                   'Cache-Control': 'no-cache',
                                                   'Connection': 'keep-alive',
                                                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
                                                   'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8'
             })
            pic = response.content
            print('读取图片 “' + link + '” 内容成功')
            flag = random.randint(0, 1000)
            name = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+str(flag)+link[-5:]
            with open('./'+name,'wb') as pp:
                pp.write(pic)
                print('存储图片 “' + link + '” 内容成功，图片名称： ' + name)
        except Exception as e:
            print(e)
            print('读取图片 “' + link + '” 内容失败')
            continue
