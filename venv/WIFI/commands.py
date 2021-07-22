#with open('aps_commands.txt') as file:
#    for ap in file:
#        print(f'show ap auto-rf 802.11a {ap}')
with open('aps_commands.txt' ) as a, open('mac_adr.txt') as b:
    for ap in a:  
        less3 = ap[3:]
        new_names = [f'JFK875'+less3]
        print(new_names)
    







        
