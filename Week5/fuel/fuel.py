def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage =convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):

        x, y = fraction.split('/')
        x,y = int(x),int(y)
        if x > y and y!=0:
            raise ValueError

        z=round(x*100/y)
        return z



def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"

    else:
        return str(percentage)+"%"


if __name__ == "__main__":
    main()