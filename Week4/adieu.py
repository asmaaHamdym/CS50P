
import inflect
p=inflect.engine()
names=[]

while True:
    try:

        names.append(input())
    except EOFError:
        print('Adieu, adieu, to',p.join(names))
        break


