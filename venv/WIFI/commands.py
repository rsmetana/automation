with open('aps_commands.txt') as file:
    for ap in file:
        print(f'show ap auto-rf 802.11a {ap}')

