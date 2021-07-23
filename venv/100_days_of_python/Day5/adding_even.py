total_even = 0
for even_number in range(2, 101, 2):
  total_even += even_number
print(total_even)

#or

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)