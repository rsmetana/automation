# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')
true = t + r + u + e
l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')
love = l + o + v + e

love_score = int(str(true) + str(love))
#or
#int_score = int(love_score)

if love_score < 10 or love_score > 90:
  print(f'Your score is {love_score}, you go together like coke and mentos')
elif love_score >= 40 and love_score <= 50:
  print(f'Your score is {love_score}, you are alright together.')
else:
  print(f'Your score is {love_score}')

#lower_case_name1 = name1.lower()
#lower_case_name2 = name2.lower()
#both_names = lower_case_name1 + lower_case_name2
#true_count = both_names.count('[t,r,u,e]')
#love_count = both_names.count('[love]')
#love_score = true_count + love_count