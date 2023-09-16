months ={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
    }

def main():
    while True:
        try:
            oldDate=input('Date: ').strip()
            s=ConverDate(oldDate)
            if s[1].isnumeric() and int(s[2])<=31 and int(s[1])<=12:
                print(f'{s[0]}-{s[1].zfill(2)}-{s[2].zfill(2)}')
                break
        except ValueError:
            month,day,year=oldDate.split(' ')
            if ',' in  day:
                day =day.rstrip(',')
                if month in months:
                    if int(day)<=31 and months[month]<=12:
                        print(f'{year}-{str(months[month]).zfill(2)}-{day.zfill(2)}')
                        break


        except TypeError:
            pass

def ConverDate(o):
    month,day,year=o.split('/')
    NewDate=[year,month,day]
    return NewDate


main()