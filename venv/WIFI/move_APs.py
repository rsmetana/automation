inventory = open('moveback.txt', 'r')
for line in inventory:
    print('config ap primary-base CORE-WLCA ' + line.split()[0] +' 10.160.0.7')
#    print('config ap secondary-base "  " ' + line.split()[0] +' 0.0.0.0')
#    print('config ap tertiary-base "  " ' + line.split()[0] +' 0.0.0.0')
    
    


#print(line.split()[0])
    

    