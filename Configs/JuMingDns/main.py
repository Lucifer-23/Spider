import os
results = open("./Results/result.txt", 'a')

ip_list = []
config_item_list = []

# 1.read ips.txt
with open('ips.txt', 'r') as file:
    for i in file.readlines():
        ip = i.strip('\n')
        ip_list.append(ip)

# 2. read all configs
with open('temple.txt', 'r') as file:
    for i in file.readlines():
        item = i.strip('\n')
        config_item_list.append(item)

# 3. generate results
with open('domains.txt', 'r') as file:
    ip_size = len(ip_list) - 1
    current_index = 0
    for i in file.readlines():
        domain = i.strip('\n')
        print('=======================')
        print('当前配置：' + domain)
        ip = ip_list[current_index]
        if current_index < ip_size:
            current_index = current_index + 1
        if current_index == ip_size:
            current_index = 0

        for item in config_item_list:
            result = item.replace('XXX', domain).replace('YYY',str(ip)) + '\n'
            print('写入数据：' + result)
            results.writelines(result)
        print('=======================')
        print('')
        print('')
        print('')
    results.close()