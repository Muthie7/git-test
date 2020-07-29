#do the difference of the ages
print('''
=============================================================================
The code takes 2 peoples ages in whichever order and finds their differences!
=============================================================================
''')

print("Give the ages for the 2 people you want to find their ages:")
pers1 = int(input())

pers2 = int(input())


if pers1 == pers2:
    print('The 2 persons are of the same age')
elif pers1 < pers2:
    diff = pers2 - pers1
    print('The age diff btwn the 2 is: ' + str(diff)+ ' with pers2 older')
elif pers2 < pers1:
    diff = pers1 - pers2
    print('The age diff btwn the 2 is: ' + str(diff) + ' with pers1 older')
else:
    print('Invalid ages')