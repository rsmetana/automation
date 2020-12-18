with open('devices.txt') as f:
    devices = f.read().splitlines()

mylist = list()
for item in devices:
    tmp = item.split(':')
    print(tmp)