inventory = open('GLSC035.txt', 'r')
for line in inventory:
    print('config ap primary-base CORE-WLCA ' + line.strip() +' 10.160.0.8')
    print('config ap secondary-base CORE-WLCA ' + line.strip() +' 0.0.0.0')



