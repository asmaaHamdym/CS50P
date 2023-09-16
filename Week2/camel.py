sen = input("camelCase: ")
#print("snake_case: ",end="")
for c in sen:
    if c.isupper():
        print(c.replace(c,'_'),end="")
    print(c.lower(), end="")