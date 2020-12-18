from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'}
ios = driver('10.1.1.10', 'user', 'password', optional_args=optional_args)
ios.open()

ios.load_replace_candidate(filename='config.txt')

dif = ios.compare_config()
print(diff)

if len(diff):
    print(diff)
    print('Commit')
    ios.commit_config()
    print('Done')
else:
    print('No Changes')
    ios.discard_config()
    
ios.close()