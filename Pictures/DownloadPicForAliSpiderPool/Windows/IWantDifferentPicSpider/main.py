# encoding: utf-8
import sys
sys.path.append('../')
from IWantDifferentPicSpider import picture_spider
import multiprocessing as mp

#设置爬取的网页数
maxIndex = 335

def loop(index):
    url = 'https://www.woyaogexing.com/touxiang/index_%d.html' % index
    print('爬取网页：' + url)
    picture_spider.pic(url)

if __name__ == '__main__':

    start_page = 334
    end_page = maxIndex

    # 多进程抓取
    pages = [i for i in range(start_page, end_page)]
    p = mp.Pool()
    p.map_async(loop, pages)
    p.close()
    p.join()