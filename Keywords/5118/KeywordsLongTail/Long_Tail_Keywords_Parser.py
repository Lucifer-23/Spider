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
        'Cookie': 'ASP.NET_SessionId=pg4gkjejc1nvf2x2xcg4lgzw; Hm_lvt_f3b3086e3d9a7a0a65c711de523251a6=1560582984; .AspNet.ApplicationCookie=P3wulUKhYL1YFMjekSbNz02AIuKj1adPA2VRZ90lSW9-1ln_iL2kH8M5rtp_zPfmZB8Csdige7FWgSY8ilqVs0fAOg1ybXh0W1S0DsoJhV-sO50G4H869x7KIHEmJDn3Wfqu_4OZnIokFgPv5i9W1v-N3yLtBuJGsrpHal7t412aXqbbIB0u-X7xLSXAIy0KwByzfizipqmfD62tLbf_MRa1lLNUkpQf9XKPSzPG8G8Sok6QKl0u3KHcJ_rGPU8JAhzh3TmF-2_XlTQNa8abzYqNI6GN6O6QA4fqbnRi73KE7e7FDJnmFB3jROkgFcKHaY5TXDawTHw9OJQtfZTaCVoT4jC_bgrTo4ORoGmX56wPdrCocd_W5SL0peYQKK63_972AK5qzihFY3oIkZ7KKyG2q_GOoFewvQM5zyhQj9UG9tLtW135PYAOCylwZ5Lw; Hm_lpvt_f3b3086e3d9a7a0a65c711de523251a6=%d'+ str(time.time())
    })
    page = urllib.request.urlopen(req,None,req_timeout)
    html = page.read()
    print('爬取网页 “' + url + '” 成功')
    return html 

def keywords(url):
    soup = BeautifulSoup(user_agent(url),'html.parser')
    allKeywords = soup.find_all(['a'])
    print('解析网页 “' + url + '” 成功')
    for item in allKeywords:
        keyword = item.get('title')

        if not keyword:
            continue
        if not keyword.strip():
            continue

        print('获取长尾关键词 “' + keyword + '” 成功')
        fp = open(".\\Results\\Results.txt", "a", encoding="utf-8")
        fp.write(keyword)
        fp.write(u"\n")
        fp.close()
