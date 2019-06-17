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
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Cookie': 'BIDUPSID=4C2E0A21C3F21347ED15DD30B87CCB55; PSTM=1560605283; H_PS_PSSID=1441_21120_29135_29238_28518_29099_29368_28831_29220; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=8FE17407A8D60FAE1AD18036C04DE247:FG=1; Hm_lvt_79a0e9c520104773e13ccd072bc956aa=1560605294; bdshare_firstime=1560605293735; Hm_lpvt_79a0e9c520104773e13ccd072bc956aa='+ str(time.time())
    })
    page = urllib.request.urlopen(req,None,req_timeout)
    html = page.read()
    print('爬取网页 “' + url + '” 成功')
    return html 

def top(url):
    try:
        soup = BeautifulSoup(user_agent(url),'html.parser')
    except Exception as e:
        print(e)
        return

    allKeywords = soup.find_all(['a'])
    print('解析网页 “' + url + '” 成功')
    for item in allKeywords:
        classLabel = item.get('class')

        if not classLabel:
            continue
        if 'list-title' not in classLabel:
            continue
        result = item.string
        print('获取热词 “' + result + '” 成功')
        fp = open(".\\Results\\Results.txt", "a", encoding="utf-8")
        fp.write(result)
        fp.write(u"\n")
        fp.close()