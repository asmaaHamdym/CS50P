def main():
    x = convert(input('What time is it? '))
    if 7<=x <=8:
        print('breakfast time')
    elif 12<=x <=13:
        print('lunch time')
    elif 12<=x <=13:
        print('lunch time')
    elif 18<=x <=19:
        print('dinner time')
    else:
        print()

def convert(time):
    hours, minutes = time.split(":")
    if time.endswith("p.m."):
        hours=float(hours)+12
        minutes= minutes.rstrip('p.m.')
    elif time.endswith("a.m."):
        minutes= minutes.rstrip('a.m.')
    time =float(hours)+float(minutes)/60
    return time

if __name__ == "__main__":
    main()