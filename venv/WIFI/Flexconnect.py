inventory = open('moveback.txt', 'r')
for line in inventory:
    print('config ap mode local ' + line.strip())
    print('y')