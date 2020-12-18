inventory = open('remain.txt', 'r')
for line in inventory:
    print('config 802.11-abgn disable ' + line.strip())
