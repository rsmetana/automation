inventory = open('GLSC035.txt', 'r')
for line in inventory:
    print('config ap primary-base CORE-WLCC ' + line.strip() +' 10.160.0.7')



