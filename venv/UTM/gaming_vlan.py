import csv

print('[gateways]')
with open('subnet.csv') as data:
    data_list = csv.reader(data)
    for row in data_list:
        site = row[0]
        subnet = row[1]
        print(site+'_Router ansible_host='+subnet.strip() +'.7.1')

with open('subnet.csv') as data:
    data_list = csv.reader(data)
    for row in data_list:
        site = row[0]
        subnet = row[1]
        print("- { site: '"+site+"_Router',  subnet: '"+subnet.strip() +".2.1 255.255.255.0' }")

with open('subnet.csv') as data:
    data_list = csv.reader(data)
    for row in data_list:
        site = row[0]
        subnet = row[1]
        print('touch '+site+'_Router.yml')
        print('echo "interfaces:')
        print('     - ios_if: "Vlan888"')
        print('       desc: "Gaming Vlan"')
        print('       enabled: true')
        print('       ipv4: '+subnet.strip() +'.2.1/24" >> ' +site+'_Router.yml')