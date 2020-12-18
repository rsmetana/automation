from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'}
ios = driver('10.1.1.10', 'user', 'password', optional_args=optional_args)
ios.open()

print(dir(ios))

ios.close()