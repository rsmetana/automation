#Lists are just a way of storing data and ordering data
#Lists use [] brackets and a comma between
#fruits = ['apple', 'kiwi', 'banana'] can be mixed contents

states_of_america = ['Delaware', 'Ohio', 'California', 'Idaho']
print(states_of_america[0:2])
#information can be sliced from variables using [] a range can be pulled using : example above. first number up to not including last number
print(states_of_america[-1])
#-1 last item in the list
states_of_america[3] = 'Oregon'
#Can replace values indexing them
states_of_america.append('Idaho')
#append to the end of a list 1 item
states_of_america.extend(['North Dakota', 'South Dakota'])
print(states_of_america)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", 
"Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", 
"Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", 
"Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", 
"Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

#You can combine multiple lists together