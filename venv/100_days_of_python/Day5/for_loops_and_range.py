#Range function basically creating a number of times you want to go through something
for number in range(1, 11, 2): #third number is how many numbers you want to skip
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)
