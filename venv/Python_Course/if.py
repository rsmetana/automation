is_male = False
is_tall = True
if is_male or is_tall:
    print('you are a male or tall or both')
elif is_male and not(is_tall):
    print('you are a short dude')
elif not(is_male) and is_tall:
    print('you are not a male but are tall')
else:
    print('you are a female and not tall')
