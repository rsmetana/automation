with open('GLSC035.txt') as inventory:
    for ap in inventory:
        print('config ap mode local '+ ap.strip())
        print('y')