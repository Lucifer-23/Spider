import urllib
import urllib.request
import re
from collections import deque
from globalVar import gloVar
from modify import modify

from bs4 import BeautifulSoup
def user_agent(url):
    req_timeout = 30
    req = urllib.request.Request(url,headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Cookie': 'BIDUPSID=B4D3C2D56B8D5D4BC1404AEDAF9698AA; PSTM=1559582131; BD_UPN=12314553; BAIDUID=AD8E9A7069A3FA066B21E2024501BA2F:FG=1; __cfduid=d190c05c41c3994c8b2ee59b2b598493c1560007730; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a03108666255; H_PS_PSSID=1436_21098_29135_29237_29098_29369_28832_29220_29131; H_PS_645EC=8dbeYMKJeIg9DA1P3Mvp%2F8zoKRPTzcVwZBugLlZpqE5kjFViWrFgAto9K%2FQ'
    })
    page = urllib.request.urlopen(req,None,req_timeout)
    html = page.read()
    print('请求百度站点查询 “' + url + '” 成功')
    return html

def site(domain):
    queue = deque()
    try:
        soup = BeautifulSoup(user_agent('http://www.baidu.com/s?wd=site:' + domain), 'html.parser')
    except Exception as e:
        print(e)
        return

    allDomainRecorders = soup.find_all(['a'])
    print('解析百度站点查询 “' + domain + '” 成功')
    for item in allDomainRecorders:
        classLabel = item.get('class')

        if not classLabel:
            continue
        if 'c-showurl' not in classLabel:
            continue

        domainRecorder = item.string
        if domainRecorder is None:
            continue
        pattern = re.compile(r'/ $')
        domainRecorder = pattern.sub('', item.string)
        print('获取百度收录域名 “' + domainRecorder + '” 成功')
        queue.append(domainRecorder)

    if not queue.__contains__(domain):
        return
    if not queue.__contains__('www.' + domain):
        return

    print('此域名 "' + domain + '" 符合百度收录要求，已保存')
    fp = open("./Results/BaiDu_Results.txt", "a", encoding="utf-8")
    fp.write(domain)
    fp.write(u"\n")
    fp.close()
    current = gloVar.current
    modify(current + 1)