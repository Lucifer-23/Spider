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
        'Cookie': 'Cookie: QiHooGUID=456EC7D4986AAEC61D51011B6D98CDB2.1560739547621; __guid=15484592.937033744676420000.1560739548295.6008; webp=1; stc_ls_sohome=RgzW2OYRK4!pTRX4hnM(Wd; __huid=117iwB8UvmJ%2B0Rm1%2BoAeiJzLctrA2wjrx%2FYx9%2F%2FlDiECk%3D; dpr=1; screenw=1; gtHuid=1; WZWS4=0dc0b0cdc087ad2c5779f74e61651207; _S=lvsltf574m0ehsv5dka15i43r2; count='+ str(requestCount)
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
