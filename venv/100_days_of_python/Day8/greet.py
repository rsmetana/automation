# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
#def greet():
#  print('Hello')
# print('This is a greeting')
#  print('!!!!!!!!!!!')

#greet()

def greet_with_name(name):
  #name variable above is the parameter
  print(f'Hello {name}')
  print(f'This is a greeting, {name}')
  print('!!!!!!!!!!!')

greet_with_name('Roman')
#name above is now the arguement

#positional argurement
def greet_with(name, location):
  print(f'Hello {name}')
  print(f'What is it like in {location}?')

greet_with('Roman', 'Ukraine')

#keyword arguement
greet_with(location='Ukraine', name='Roman')