from datetime import date
import inflect
import re
import sys

def main():
   print(convert(input("Date of Birth: ")), 'minutes')

def convert(Date):
    if re.fullmatch(r'[0-9]{4}-[0-1][0-9]-[0-3][0-9]', Date.strip()):
        Today = date.today()
        Date = date.fromisoformat(Date)
        age = Today - Date
        p = inflect.engine()
        return p.number_to_words(age.days*24*60, andword="").capitalize()

    else:
        sys.exit('Invalid date')
if __name__ == "__main__":
    main()












