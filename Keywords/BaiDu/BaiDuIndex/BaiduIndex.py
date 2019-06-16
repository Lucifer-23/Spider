import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from random import choice, randint
import re
import json
import xlwt
import shutil
import os,random
import chardet
import time

area = '0'
days = '30'
workbook = xlwt.Workbook()
worksheetData = workbook.add_sheet('data')
worksheetData.write(0, 0, label='关键词')
worksheetData.write(0, 1, label='整体搜索指数')
worksheetData.write(0, 2, label='移动搜索指数')
worksheetData.write(0, 3, label='PC搜索指数')
i = 1

with open('website.txt', 'r') as f:
	for j in f.readlines():
		keywrod = j.replace('\n', '')
		url = 'http://index.baidu.com/api/SearchApi/index?word=' + \
			quote(keywrod, encoding='utf8') + '&area=' + area + \
			'&days=' + days
		try:
			print('===================================================')
			print('查询关键词 "' + keywrod + '"')
			session = requests.Session()
			headers = { 'Host':'index.baidu.com',
                        'Connection':'keep-alive',
                        'Accept': 'application/json, text/plain, */*',
                        'X-Requested-With': 'XMLHttpRequest',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                        'Referer': 'http://index.baidu.com/v2/main/index.html',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'zh-CN,zh;q=0.9',
                        'Cookie': 'BAIDUID=16C8AF3E08D8DA9D9E532825BFF9BB16:FG=1; BIDUPSID=16C8AF3E08D8DA9D9E532825BFF9BB16; PSTM=1559042305; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1460_21080_18560_29135_29238_28519_29099_29139_28838_29220; BDSFRCVID=OB8sJeCCxG3JggRw0WaSW-cjekFOeQZRddMu3J; H_BDCLCKID_SF=tR30WJbHMTrDHJTg5DTjhPrMXPKObMT-027OKKOF5b3CfIJ5-qbRqttqbfRlW-QIyHrb0p6athF0HPonHjLBDTc33J; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1560178783,1560179170,1560324621,1560325083; bdshare_firstime=1560326168563; CHKFORREG=02dbebcff556c8cba814147dc164826a; delPer=0; PSINO=7; BDUSS=RVZU12MEFIZlc5ZklnUExhQlRwQ2NCUXNDVi1IRTF-bjk2ZWptTmdZYWtSeWhkSVFBQUFBJCQAAAAAAAAAAAEAAABu9l3rvOW1sM3PsNEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKS6AF2kugBdVF; bdindexid=g64c9p0b214sute3h4b6jka916; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=' + str(time.time())
						}
			req = session.get(url, headers=headers, timeout=60)
			dataJson = json.loads(req.content)
			data = dataJson['data']
			pvData = data['generalRatio'][0]
			all = pvData['all']['avg']
			pc = pvData['pc']['avg']
			wise = pvData['wise']['avg']
			worksheetData.write(i, 0, label=keywrod)
			worksheetData.write(i, 1, label=all)
			worksheetData.write(i, 2, label=wise)
			worksheetData.write(i, 3, label=pc)
			print('关键词 "' + keywrod + '" 数据写入成功')
			i = i + 1
		except Exception as e:
			print(e)
		finally:
			print('查询下一个关键词')
			print('===================================================')
			print('')
			print('')
			print('')

file = time.strftime('Baidu_Index' + "%Y-%m-%d-%H_%M_%S-", time.localtime()) + area + '-'+ days + '.xlsx'
workbook.save(file)