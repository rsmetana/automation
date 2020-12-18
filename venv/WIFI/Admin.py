inventory = open('rest.txt', 'r')
for line in inventory:
    print('config ap tertiary-base " " ' + line.strip() +' 0.0.0.0')
    print('config ap secondary-base " " ' + line.strip() +' 0.0.0.0')
    print('config ap primary-base CORE-WLCC ' + line.strip() +' 10.160.0.7')