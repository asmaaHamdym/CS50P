import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
   n = re.findall(r'.*\bum\b.*',s.strip())
   m = re.findall(r'.*\bUm\b.*',s.strip())
   return len(n+m)

if __name__ == "__main__":
    main()