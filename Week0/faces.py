def convert(str):
    x = str.replace(':(','🙁').replace(':)','🙂')
    return x
def main():
    o = input()
    print(convert(o))


main()