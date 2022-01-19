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
        print('    edit "'+ site.strip() +'_Gaming_Vlan"')
        print('        set subnet ' + subnet.strip() +'.2.0 255.255.255.0')
        print('    next')

print('''end\n 
config firewall addrgrp\n
    edit "Gaming_Vlans"''')

with open('subnet.csv') as data:
    data_list = csv.reader(data)
    for row in data_list:
        site = row[0]
        subnet = row[1]
        print(f'"{site}_Gaming_Vlan" ', end=" ")
print('    next\nend')
