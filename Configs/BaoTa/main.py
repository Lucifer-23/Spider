import os
import time

results = open(time.strftime('./Results/' + "%Y-%m-%d-%H_%M_%S-result.txt", time.localtime()), 'w')

temples = ''
mirror_list = []

# 1. read temple
with open('temple.txt', 'r', encoding='UTF-8') as file:
    for i in file.readlines():
        temples += i

# 1. read mirror
with open('mirror.txt', 'r', encoding='UTF-8') as file:
    for i in file.readlines():
        item = i.strip('\n')
        mirror_list.append(item)

with open('domains.txt', 'r', encoding='UTF-8') as file:
    index = 0;
    for i in file.readlines():
        name = i.strip('\n')
        results.writelines('============ config for ' + name + ' start ============')
        results.writelines('\n')
        mirror_config = mirror_list[index].split('：')
        str = temples.replace('AAA', name)\
              .replace('BBB', mirror_config[0])\
              .replace('CCC', mirror_config[1])\
              .replace('DDD', mirror_config[0])\
              + '\n'
        results.writelines(str)
        results.writelines('============ config for ' + name + ' end ============')
        results.writelines('\n')
        results.writelines('\n')
        results.writelines('\n')
        index = index + 1
    results.close()
