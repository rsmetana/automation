inventory = open('GLSC035.txt', 'r')
for line in inventory:
    print('config ap group-name WW616 '+ line.strip())
    print('y')