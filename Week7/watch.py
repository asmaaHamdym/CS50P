import re
import sys


def main():
    print(parse(input("HTML: ").strip()))

''' Supported Formats:
http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0

desired ouput:
https://youtu.be/xvFZjo5PgG0
'''
def parse(s):
    if matches := re.search(r'^<iframe.+https?://(www\.)?youtube\.com/embed/(\w+)',s, re.IGNORECASE):
        url='https://youtu.be/'+matches.group(2)
        return url

if __name__ == "__main__":
    main()