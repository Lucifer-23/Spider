import requests
import jieba
import xlwt
import shutil
import time

workbook = xlwt.Workbook()
worksheet_statistics = workbook.add_sheet('data')
worksheet_statistics.write(0, 0, label='站点')
worksheet_statistics.write(0, 1, label='是否为静态站')
worksheet_statistics.write(0, 2, label='关键词排名')
worksheet_statistics.write(0, 3, label='关键词')
index = 1

def detection_statistics(domain):
    response = requests.get(domain,
                            headers = {'Connection': 'Keep-Alive',
                                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                       'Accept-Language': 'zh-CN,zh;q=0.9',
                                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
                                       },
                            timeout=10)
    website_content = str(response.content.decode("utf-8"))
    print('获取站点 "' + domain + '" 内容成功')
    worksheet_statistics.write(index, 0, label=domain)
    static_html_count = website_content.count('htm') / 2
    print('站点 "' + domain + '" 含有静态网页个数： ' + str(static_html_count))

    if static_html_count > 20:
        print('站点 "' + domain + '" 为静态站点')
        worksheet_statistics.write(index, 1, label='是')
    else:
        worksheet_statistics.write(index, 1, label='否')


    original_data = list(jieba.cut(website_content))
    words_dict = {}
    words_set = set(original_data)
    for word in words_set:
        if is_all_chinese(word):
            if len(word) > 1:
                words_dict[word] = original_data.count(word)

    words_rank_dict = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)

    keywords_statistics = ''
    keywords = ''
    for i in range(5):
        top_word = words_rank_dict[i];
        keywords_statistics = keywords_statistics + str(top_word) + '\n'
        keywords = keywords + top_word[0] + ','

    worksheet_statistics.write(index, 2, label=keywords_statistics)
    worksheet_statistics.write(index, 3, label=keywords)

def is_all_chinese(text):
    for character in text:
        if not ('\u4e00' <= character <= '\u9fa5'):
            return False
    return True

with open('domains.txt', 'r') as f:
    for site_url in f.readlines():
        domain = site_url.replace('\n', '')
        print('开始检查站点：' + domain)
        detection_statistics(domain)
        index = index + 1

file = time.strftime('Site_Statistics_' + "%Y-%m-%d-%H_%M_%S-", time.localtime()) + '.xlsx'
workbook.save(file)