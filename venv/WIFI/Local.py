inventory = open('GLSC035.txt', 'r')
for line in inventory:
    print('config ap mode local ' + line.strip())
    print('y')