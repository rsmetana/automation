with open('interfaces.txt') as interfaces:
    for interface in interfaces:
        print(f'config interface dhcp dynamic-interface {interface.strip()} primary 10.251.3.8 secondary 10.251.3.9')
