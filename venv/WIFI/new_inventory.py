with open('inventory.txt') as file:
    for line in file:
        print(f'config wlan apgroup interface-mapping delete '+ line.strip() +' 1')
        print('config wlan apgroup interface-mapping delete ' + line.strip() + ' 2')
        print('config wlan apgroup interface-mapping delete ' + line.strip() + ' 17')
        print('config wlan apgroup interface-mapping delete ' + line.strip() + ' 21')
        print('config wlan apgroup interface-mapping add ' + line.strip() + ' 1 ' + line.strip() + '-internal')
        print('config wlan apgroup interface-mapping add ' + line.strip() + ' 2 ' + line.strip() + '-mobile')
        print('config wlan apgroup interface-mapping add ' + line.strip() + ' 17 ' + line.strip() + '-mobile')
        print('config wlan apgroup interface-mapping add ' + line.strip() + ' 21 ' + line.strip() + '-mobile')


