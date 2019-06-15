import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from random import choice, randint
from userAgents import agents
import re
import json
import xlwt
import shutil
import os,random
import chardet
import time

workbook = xlwt.Workbook()
worksheetData = workbook.add_sheet('status')
worksheetData.write(0, 0, label='站点域名')
worksheetData.write(0, 1, label='当前状态码')
worksheetData.write(0, 2, label='站点信息')
i = 1

with open('websites.txt', 'r') as f:
	for j in f.readlines():
		website = j.replace('\n', '')
		try:
			print('===================================================')
			print('查询站点 "' + website + '"')
			session = requests.Session()
			headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
			response= requests.get(website, headers=headers, timeout=5)
			print('站点 "' + website + '" 状态码：%d' %response.status_code)
			if response.status_code == 200:
				print('站点 "' + website + '" 访问正常')
			else:
				print('站点 "' + website + '" 访问异常')
				worksheetData.write(i, 2, label=response.content)
			worksheetData.write(i, 0, label=website)
			worksheetData.write(i, 1, label=response.status_code)
			i = i + 1
		except Exception as e:
			print('站点 "' + website + '" 访问异常：')
			print(response.content)
			print(e)
			worksheetData.write(i, 0, label=website)
			worksheetData.write(i, 1, label=response.status_code)
			worksheetData.write(i, 2, label=e.__str__())
			i = i + 1
		finally:
			print('查询下一个站点')
			print('===================================================')
			print('')
			print('')
			print('')

file = 'Check_Websites' + time.strftime("%Y-%m-%d-%H_%M_%S-", time.localtime()) + '.xlsx'
workbook.save(file)