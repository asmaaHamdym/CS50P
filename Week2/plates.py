def main():
    #input a vanity plate from user and ensure lower case
    plate = input("Plate: ").lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) in range(2,7): #ensure min. and max. charcter
        if s[:2].isalpha() and  s.isalnum() :
            if Checknumber(s) :
                if  CheckZero(s):
                    return True
            else:
                return False

def Checknumber(s):
    for c in range(len(s)):
        if s[c].isnumeric():
            if not s[c:].isnumeric():
                return False
    return True

def CheckZero(s):
    try:
        zeroIndex=s.index('0')
        if not s[zeroIndex-1].isnumeric():
            return False
        else:return True
    except ValueError:
        return True

main()