import os

results = open("./Results/result.txt", 'w')

with open('domains.txt', 'r') as file:
    for i in file.readlines():
        name = i.strip('\n')
        str = 'www.XXX|XXX|80|D:\Pearce2\XXX'.replace('XXX', name) + '\n'
        results.writelines(str)
    results.close()
