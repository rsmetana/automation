import csv

print('config firewall address')
with open('subnet.csv') as data:
    data_list = csv.reader(data)
    for row in data_list:
        site = row[0]
        subnet = row[1]
        #print(f'''edit "{site}_Games"
        #set type iprange
        #set start-ip {subnet}.11.1
        #set end-ip {subnet}.11.10''')
        print('    edit "'+ site.strip() +'_Games"')
        print('        set type iprange')
        print('        set start-ip '+ subnet.strip() +'.11.1')
        print('        set end-ip ' + subnet.strip() +'.11.25')
        print('    next')
print('''end\n 
config firewall addrgrp\n
    edit "ONLINE-GAMES"''')


member_set = []
with open('subnet.csv') as data:
    data_list = csv.reader(data)
    for row in data_list:
        site = row[0]
        subnet = row[1]
        print(f'"{site}_Games" ', end=" ")
print('    next\nend')

