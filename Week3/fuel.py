def main():
    a =percentage()

    if a<=1:
        print('E')
    elif a>=99:
        print('F')

    else:
        print(a,'%',sep='')


def percentage():
    while True:
        try:
            l,m =input('Fraction: ').split('/')
            x,y = int(l),int(m)
            if x<=y:
                return round(x*100/y)
        except (ValueError, ZeroDivisionError):
            pass







main()