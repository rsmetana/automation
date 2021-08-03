import csv

with open('jfk.csv' ) as a:
    for ap in a:  
        less3 = ap[3:]
        new_names = [f'JFK875'+less3]
        print('config ap name'+ new_names[0]+ '' +new_names[1])