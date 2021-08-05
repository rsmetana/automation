name = 'roman' #name is a variable. data typing is dynamic. meaning it can mean different things when you apply it.
print('my name is', name)

names = ['david', 'roman', 'peter', 'jane'] # identified by [] list sequences of items.
print('the names are', names[0:]) #can be indexed 

for name in names:
    print('the current name is', name) # for loop run this for each item in list

persons = [{'name': 'david', 'location': 'UK', 'handsome': True, 'intelligent': 'maybe'},
           {'name': 'roman', 'location': 'UA', 'handsome': False, 'intelligent': 'nope'},
           {'name': 'peter', 'location': 'USA', 'handsome': True, 'intelligent': 'kinda'},
           {'name': 'jane', 'location': 'FRA', 'handsome': True, 'intelligent': 'yes'}] # dictionary within a list. Dict are identified by {} 
for person in persons:
    print(f'the current person is {person}') # fstring literal.