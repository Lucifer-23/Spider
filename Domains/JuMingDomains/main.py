# encoding: utf-8
'''
Created on 2019年06月17日

@author: Pearce
'''
import sys
sys.path.append('../')
import time
import urllib
import urllib.request
from JuMingDomains import BaiDuSite
from JuMingDomains import ThreeSixZeroSite
from bs4 import BeautifulSoup
from globalVar import gloVar

suffix = 'cn'
deadline = 90
price = 100
items = 500
page = 1
url = 'http://www.juming.com/ykj/?api_sou=1&jgpx=0&1=1&ymlx=0&ymhz={0}&dqsj={1}&qian2={2}&meiye={3}&page={4}&_='.format(suffix,deadline,price,items,page) + str(int(time.time()))
max = 1

def user_agent(url):
    req_timeout = 30
    req = urllib.request.Request(url,headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Cookie': 'Juming%2Ecom=new%5Fbanban%5Fzhu=1; t%5Ftuiguang=bb%5F19; ASPSESSIONIDSQTATQCC=GABBCLDDCJLALAJBBAANNFGO; UM_distinctid=16b638ac8b21e0-0a0d060fcfd8c1-7a1437-1fa400-16b638ac8b386f; CNZZDATA3432862=cnzz_eid%3D1218762686-1560742474-null%26ntime%3D1560742474; IESESSION=alive; pgv_pvi=9685315584; pgv_si=s7526146048; _qddaz=QD.tch1lo.vp1tzx.jwzu6oi4; _qdda=3-1.3oloaq; _qddab=3-bzfmr0.jwzu6oi6; _qddamta_4009972996=3-0; tencentSig=3577349120; skinName=null; Hm_lpvt_512ed551fae9428abd7d743009588c7a=' + str(time.time())
    })
    page = urllib.request.urlopen(req,None,req_timeout)
    html = page.read()
    print('请求聚名网查询 “' + url + '” 成功')
    return html


def checkSite(domain):
    print('当前检查：' + domain)
    BaiDuSite.site(domain)
    ThreeSixZeroSite.site(domain)

def loop(url):
    soup = BeautifulSoup(user_agent(url), 'html.parser')
    check_non_data = soup.find_all("td", {"colspan": "9"})
    print('解析聚名网查询 “' + url + '” 成功')
    for item in check_non_data:
        msg = item.string
        if msg == '没有找到记录.':
            print(msg)
            return

    all_domains = soup.find_all("a", {"class": "domainsc"})
    current = gloVar.current
    for item in all_domains:
        domain = item.string
        if domain is None:
            continue
        checkSite(domain)
        current = gloVar.current
        print('已挖得 ' + str(current) + ' 个域名')
        if current >= max:
            return

    if current < max:
        global page
        page = page + 1
        next_url = 'http://www.juming.com/ykj/?api_sou=1&jgpx=0&1=1&ymlx=0&ymhz={0}&dqsj={1}&qian2={2}&meiye={3}&page={4}&_='.format(suffix, deadline, price, items, page)+ str(int(time.time()))
        loop(next_url)

loop(url)