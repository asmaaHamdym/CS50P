import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        if  matches:=re.search(r'^([0-9]*)\.([0-9]*)\.([0-9]*)\.([0-9]*)$',ip):
            if all(int(group) in range(0,256) for group in matches.groups()):
                return True
            else: return False
        else: return False


    except (ValueError):
        return False


if __name__ == "__main__":
    main()