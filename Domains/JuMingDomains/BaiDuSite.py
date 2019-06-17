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
        'Cookie': 'BAIDUID=5F57EA80E756EE6AFDF2D0FC0C32477D:FG=1; PSTM=1555051522; BD_UPN=12314753; H_PS_PSSID=26523_1448_21126_29135_29237_28519_29099_29369_28835_29221; BIDUPSID=D1C0E95614FAD71F9C58E1A5EF8BF97B; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_645EC=9a86svqwaticxesYXy%2B5JCFGUlFnaoCCrj1jPvjH2RYADPJ0BZatgmpoHpM'
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