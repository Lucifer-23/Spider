import urllib
import urllib.request
from collections import deque

from bs4 import BeautifulSoup

requestCount = 0
def user_agent(url):
    req_timeout = 30
    req = urllib.request.Request(url,headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Cookie': 'QiHooGUID=5890F1A4E8031F2E8EC55E57F7CE747B.1560770770858; _S=rpdttism73rbua32sdqtsll0o6; __guid=15484592.1875221759665618700.1560770767694.5598; webp=1; stc_ls_sohome=RgzW2OYRK4!pTRX4hnM(Wd; __huid=11ST5pSO8AB7S5sMtPTAZ3%2BoPvzth9glqdr9AoCkzUnJY%3D; gtHuid=1; WZWS4=22ce5c1503dcd3508a326d910ce93349; count='+ str(requestCount)
    })
    page = urllib.request.urlopen(req,None,req_timeout)
    html = page.read()
    print('请求360站点查询 “' + url + '” 成功')
    return html 

def site(domain):
    global requestCount
    requestCount = requestCount + 1
    queue = deque()
    soup = BeautifulSoup(user_agent('https://www.so.com/s?ie=utf-8&fr=none&src=360sou_newhome&q=site:' + domain), 'html.parser')
    allDomainRecorders = soup.find_all("p", {"class": "res-linkinfo"})
    print('解析360站点查询 “' + domain + '” 成功')
    for item in allDomainRecorders:
        cite = item.find('cite')
        if cite is None:
            continue
        domainRecorder = cite.string
        if domainRecorder is None:
            continue
        print('获取360收录域名 “' + domainRecorder + '” 成功')
        queue.append(domainRecorder)

    if not queue.__contains__(domain):
        return
    if not queue.__contains__('www.' + domain):
        return

    print('此域名 "' + domain + '" 符合360收录要求，已保存')
    fp = open("./Results/360_Results.txt", "a", encoding="utf-8")
    fp.write(domain)
    fp.write(u"\n")
    fp.close()
