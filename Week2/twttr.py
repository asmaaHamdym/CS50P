
SEN=input('Input: ')
letters = ['a', 'e', 'i', 'o','u']
for c in SEN:
    if c.lower() in letters:
        print(c.replace(c,''),end="")
    else:
        print(c,end="")
print()