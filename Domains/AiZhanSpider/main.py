# encoding: utf-8
'''
Created on 2019年06月17日

@author: Pearce
'''
import time
import urllib
import urllib.request
from bs4 import BeautifulSoup
import xlwt
import shutil

max = 1

workbook = xlwt.Workbook()
sheet_keywords = workbook.add_sheet('keywords')
sheet_keywords.write(0, 0, label='关键词')
sheet_keywords.write(0, 1, label='百度指数')
sheet_keywords.write(0, 2, label='360指数')

sheet_domains = workbook.add_sheet('domains')
sheet_domains.write(0, 0, label='域名')
sheet_domains.write(0, 1, label='网站标题')
sheet_domains.write(0, 2, label='网站关键词')
sheet_domains.write(0, 3, label='网站描述')

keywords_index = 1
domains_index = 1

def user_agent(url):
    req_timeout = 30
    req = urllib.request.Request(url,headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Cookie': ' _csrf=c138eb9d5d0953be1293991e73f9f7690ffbb3220490d476dd2c273a86359641a:2:{i:0;s:5:"_csrf";i:1;s:32:"2NI6Om6ha0-jzV0rzSun_c-ojoCFVCqX";}; allSites=www.52pojie.cn|photo.blog.sina.com.cn|www.kabkd.cn|www.wuchangtoumi.com|www.xiangmudaba.com|siff.com|diaosu.cn|wojine.com|www.cesafe.com|www.360shouzhuan.com|110hack.com; Hm_lpvt_b37205f3f69d03924c5447d020c09192=' + str(time.time())
    })
    page = urllib.request.urlopen(req,None,req_timeout)
    html = page.read()
    print('请求 “' + url + '” 成功')
    return html


def website_info(domain):
    global domains_index
    print('开始获取 "' + domain + '" 数据')

    cha_website_url = 'https://www.aizhan.com/cha/%s/' %domain

    try:
        soup = BeautifulSoup(user_agent(cha_website_url), 'html.parser')
    except Exception as e:
        print(e)
        return

    print('获取 "' + domain + '" 数据成功')
    sheet_domains.write(domains_index, 0, label=domain)

    # parse title keyword description
    datas = soup.find_all("span")
    for item in datas:
        id = item.get('id')
        if id is None:
            continue
        if id == 'webpage_tdk_title':
            sheet_domains.write(domains_index, 1, label=item.string)
        if id == 'webpage_tdk_keywords':
            sheet_domains.write(domains_index, 2, label=item.string)
        if id == 'webpage_tdk_description':
            sheet_domains.write(domains_index, 3, label=item.string)

    domains_index = domains_index + 1

def loop(url, index):
    page_url = url %index
    try:
        soup = BeautifulSoup(user_agent(page_url), 'html.parser')
    except Exception as e:
        print(e)
        if index < max:
            loop(url, index + 1)
        return

    print('解析爱站网 “' + page_url + '” 成功')

    all_domains = soup.find_all(["a"])
    for item in all_domains:
        href_url = item.get('href')
        if href_url is None:
            continue
        if not href_url.startswith('https://www.aizhan.com/cha/www'):
            continue

        domain = item.string
        if domain is None:
            continue
        website_info(domain)

    if index < max:
        loop(url, index + 1)

if __name__ == '__main__':

   loop('https://www.aizhan.com/bigdata/pcrankup/%d/', 1)
   #loop('https://www.aizhan.com/bigdata/pcwordup/%d/', 1)
   #loop('https://www.aizhan.com/bigdata/pcipup/%d/', 1)
   #loop('https://www.aizhan.com/bigdata/indexup/%d/', 1)

   file = time.strftime('AiZhan_Statistics_' + "%Y-%m-%d-%H_%M_%S-", time.localtime()) + '.xlsx'
   workbook.save(file)
   print('保存数据成功')
