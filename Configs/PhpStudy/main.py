import os
import time

results = open(time.strftime('./Results/' + "%Y-%m-%d-%H_%M_%S-result.txt", time.localtime()), 'w')

with open('domains.txt', 'r') as file:
    for i in file.readlines():
        name = i.strip('\n')
        str = 'www.XXX|XXX|80|D:\Tom\Group1\XXX'.replace('XXX', name) + '\n'
        results.writelines(str)
    results.close()
