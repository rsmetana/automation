inventory = open('moveback.txt', 'r')
for line in inventory:
    print('config ap mode local ' + line.split()[0])
    print('y')