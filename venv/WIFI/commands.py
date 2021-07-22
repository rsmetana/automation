#with open('aps_commands.txt') as file:
#    for ap in file:
#        print(f'show ap auto-rf 802.11a {ap}')
names_list = []
with open('aps_commands.txt' ) as a:
    for ap in a:  
        less3 = ap[3:]
        new_names = (f'JFK875'+less3)
        names_list.append(new_names.strip())
#print(names_list)
mac_list = []
with open('mac_adr.txt') as b:
    for mac in b:
        str(mac_list.append(mac.strip()))
#print(mac_list)


info = dict(zip(names_list, mac_list))
name_mac = []
for names, macs in info.items():
   name_mac.append(names +' '+ macs)

#print(name_mac)
for item in name_mac:
    print(f'config ap name {item}')

for item in names_list:
    print(f'config ap group-name JFK875 {item}''\n y')


    


        
