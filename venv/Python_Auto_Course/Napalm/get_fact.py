from napalm import get_network_driver
import json
driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'}
ios = driver('10.1.1.10', 'user', 'password', optional_args=optional_args)
ios.open()

output = ios.get_facts()
dump = json.dumps(output, sort_keys=True, indent=4)

output = ios.
dump = json.dumps(output, sort_keys=True, indent=4)

ios.close()