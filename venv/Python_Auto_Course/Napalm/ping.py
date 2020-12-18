from napalm import get_network_driver
import json
driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'}
ios = driver('10.1.1.10', 'user', 'password', optional_args=optional_args)
ios.open()

output = ios.ping('10.1.1.20')
ping = json.dumps(output, sort_keys=True, indent=4)

ios.close()