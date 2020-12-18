from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'}
ios = driver('10.1.1.10', 'user', 'password', optional_args=optional_args)
ios.open()

output = ios.get_arp_table()
for item in output:
    print(item)

dump = json.dumps(output, sort_keys=True, indent=4)

#print(dump)
with open('arp.txt', 'w') as f:
    f.write(dump)

ios.close()