from re import fullmatch
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches:=fullmatch(r'([0-9][0-9]?):?([0-9][0-9])? (AM|PM) to ([0-9][0-9]?):?([0-9][0-9])? (AM|PM)',s.strip()):
        # conversion of From_time
        if int(matches.group(1))not in range(1,13) or int(matches.group(4)) not in range(1,13):
            raise ValueError
        if matches.group(2) and int(matches.group(2)) not in range(0,60):
                raise ValueError
        if matches.group(3)=='PM':
            if matches.group(1)=='12':
                pmHour= 12
            else:pmHour = int(matches.group(1)) + 12
            From = str(pmHour) + ':' + (matches.group(2) if matches.group(2) else '00')

        elif matches.group(3)=='AM':           #
            if matches.group(1)=='12':
                amHour= '00'
            elif len(matches.group(1))==1:
                amHour = '0' + matches.group(1)
            From = amHour + ':' + (matches.group(2) if matches.group(2) else '00')

        # conversion of To_time
        if matches.group(5) and int(matches.group(5)) not in range(0,60):
                raise ValueError
        if matches.group(6)=='PM':
            if matches.group(4)=='12':
                pmHour= 12
            else:pmHour = int(matches.group(4)) + 12
            To = str(pmHour) + ':' + (matches.group(5) if matches.group(5) else '00')

        elif matches.group(6)=='AM':
            if matches.group(4)=='12':
                amHour= '00'
            elif len(matches.group(4))==1:
                amHour = '0' + matches.group(4)
            To = amHour + ':' + (matches.group(5) if matches.group(5) else '00')
        return From + ' to ' + To
    else:
        raise ValueError



if __name__ == "__main__":
    main()