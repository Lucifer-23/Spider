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

suffix = 'com'
deadline = 90
price = 60
items = 500
page = 1
url = 'http://www.juming.com/ykj/?api_sou=1&jgpx=0&1=1&ymlx=0&ymhz={0}&dqsj={1}&qian2={2}&meiye={3}&page={4}&_='.format(suffix,deadline,price,items,page) + str(int(time.time()))
max = 130

def user_agent(url):
    req_timeout = 33
    req = urllib.request.Request(url,headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Cookie': 'UM_distinctid=16b233d3be84f-0a020c5136d88c-3e385904-144000-16b233d3be9328; _qddaz=QD.sivftz.7jyzai.jwhzvqby; tencentSig=1248078848; pgv_pvi=5092662272; t%5Ftuiguang=bb%5F14dt; ASPSESSIONIDQQRDTQDD=EODJIEODFNPCGBCFCMBJHMAD; CNZZDATA3432862=cnzz_eid%3D991459120-1559659197-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1560850505; Hm_lvt_512ed551fae9428abd7d743009588c7a=1559752426,1559910547,1560790011,1560854471; Hm_lvt_f94e107103e3c39e0665d52b6d4a93e7=1559752426,1559910547,1560790012,1560854471; IESESSION=alive; pgv_si=s2201974784; _qdda=3-1.1vq7d; _qddab=3-dfv6by.jx1ogans; _qddamta_4009972996=3-0; Juming%2Ecom=islogincode=4ce7f2aa13c88450b6&login%5Fuid=308587&new%5Fbanban%5Fzhu=1; Hm_lpvt_512ed551fae9428abd7d743009588c7a=1560854483; Hm_lpvt_f94e107103e3c39e0665d52b6d4a93e7=' + str(time.time())
    })
    page = urllib.request.urlopen(req,None,req_timeout)
    html = page.read()
    print('请求聚名网查询 “' + url + '” 成功')
    return html


def checkSite(domain):
    print('当前检查：' + domain)
    BaiDuSite.site(domain)
    #ThreeSixZeroSite.site(domain)

def loop(url):
    try:
      soup = BeautifulSoup(user_agent(url), 'html.parser')
    except Exception as e:
        print(e)
        loop(url)
        return
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