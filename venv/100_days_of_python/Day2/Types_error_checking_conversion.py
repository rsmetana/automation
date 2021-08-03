#first example wont work
#print(len(456))
#Second example will since data type is converted to string or casting
print(len(str(245)))
#example
num_char = len(input('what is your name? '))
print('your name has ' + str(num_char) + ' characters in it!')
#or
new_num_char = str(num_char)
print('your name has ' + new_num_char + ' characters in it!')
#type() allows you to check what data type something is
print(type(num_char))

a = 123
print(type(a))
a = str(123)
print(type(a))
a = float(123)
print(type(a))

print(70 + float('100.5'))
print(str(70) + str(100))