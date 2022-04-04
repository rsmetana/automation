inventory = open('JA_APs.txt', 'r')
for line in inventory:
    print('config ap group-name JM292 '+ line.strip())
    print('y')