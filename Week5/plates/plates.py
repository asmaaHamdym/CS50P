def main():
    # input a vanity plate from user and ensure lower case
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (
        len(s) in range(2, 7)
        and s[:2].isalpha()
        and s.isalnum()
        and Checknumber(s)
        and CheckZero(s)
    ):
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
        zeroIndex = s.index("0")
        if not s[zeroIndex - 1].isnumeric():
            return False
        else:
            return True
    except ValueError:
        return True


if __name__ == "__main__":
    main()
