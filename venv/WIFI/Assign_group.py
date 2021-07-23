inventory = open('JA_APs.txt', 'r')
for line in inventory:
    print('config ap group-name JH284 '+ line.strip())
    print('y')