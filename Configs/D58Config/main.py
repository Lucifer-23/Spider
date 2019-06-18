import os
results = open("./Results/result.txt", 'a')

mirror_list = []
title_list = []
keyword_list = []
description_list = []
theirs_list = []
ours_list = []

temple = 'AAA||BBB||CCC||DDD||EEE||FFF||GGG'

# 1.read mirror
with open('mirror.txt', 'r') as file:
    for item in file.readlines():
        mirror_list.append(item.strip('\n'))

# 2. read title
with open('title.txt', 'r') as file:
    for item in file.readlines():
        title_list.append(item.strip('\n'))

# 3. read keyword
with open('keyword.txt', 'r') as file:
    for item in file.readlines():
        keyword_list.append(item.strip('\n'))

# 4. read description
with open('description.txt', 'r') as file:
    for item in file.readlines():
        description_list.append(item.strip('\n'))

# 5. read theirs
with open('theirs.txt', 'r') as file:
    for item in file.readlines():
        theirs_list.append(item.strip('\n'))

# 6. read ours
with open('ours.txt', 'r') as file:
    for item in file.readlines():
        ours_list.append(item.strip('\n'))

# 7. generate results
with open('domains.txt', 'r') as file:
    current_index = 0
    for i in file.readlines():
        domain = i.strip('\n')
        print('=======================')
        print('当前配置：' + domain)
        result = temple.replace('AAA', domain)                         \
                       .replace('BBB',mirror_list[current_index])      \
                       .replace('CCC',title_list[current_index])       \
                       .replace('DDD', keyword_list[current_index])    \
                       .replace('EEE', description_list[current_index])\
                       .replace('FFF', theirs_list[current_index])     \
                       .replace('GGG', ours_list[current_index])       \
                       + '\n'
        print('写入数据：' + result)
        results.writelines(result)
        current_index = current_index + 1
        print('=======================')
        print('')
        print('')
        print('')
    results.close()