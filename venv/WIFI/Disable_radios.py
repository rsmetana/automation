inventory = open('remain.txt', 'r')
for line in inventory:
    print('config 802.11a disable ' + line.strip())
    print('config 802.11b disable ' + line.strip())
