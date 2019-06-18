import urllib
import urllib.request

import time 
from bs4 import BeautifulSoup
def user_agent(url):
    req_timeout = 30
    req = urllib.request.Request(url,headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Cookie': 'Hm_lvt_f3b3086e3d9a7a0a65c711de523251a6=1560860965; ASP.NET_SessionId=qexqaizugay1yek3zkrqae2d; .AspNet.ApplicationCookie=JkjX_FEb5i20XtHpelfsBu_vQ26x0zJ3HolxKaLDSKxM5MWZKwmFABI1nO16cn5RXCrLdpVe_6XJ1LhLHzl72nRtG_jWGZEc8pZBvkkRB2gk8VFaFb0j1vBtcm-_6FOxkz_7r0e0eqjBHJCf2dj-asBxbYwtyOPYseyjLQXMwuWW-lxZLguYqOSd__piGvBh-plBs-TxwuHeQV8r0Q9WRG1NKfJ_fI06eIlOFwhusBm6gDDuArsEh0RbAMSCTgUTZ2ge4Li4wXsjzKvKzU2_QSIAyYoEXOawUs1Y3WMHkhVr3BHqrNDbd3vaI2_SsI2gN6Mu_dDtrb2aaHe-fW9-pEmJwrgmtLSgITdv9yaVKFAli78je1kR1MqeW9kGN1zF1oHNsicHzuV-JyTkXZJ19diK_yc5q5iC_br_IqI7I08; Hm_lpvt_f3b3086e3d9a7a0a65c711de523251a6='+ str(time.time())
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
        fp = open("./Results/Results.txt", "a", encoding="utf-8")
        fp.write(keyword)
        fp.write(u"\n")
        fp.close()
