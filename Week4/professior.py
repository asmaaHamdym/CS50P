import random
import sys

def main():
    score=0
    level=get_level()
    for i in range(0,10):
        tries=3
        try:
            x=generate_integer(level)
            y=generate_integer(level)
            result=x+y

            while tries>0:
                user_result=input(f'{x} + {y} =')
                if result==int(user_result):
                    score += 1
                    break
                elif result!=int(user_result):
                    print("EEE")
                    tries-= 1
                    continue

            if tries==0:
                    print(f'{x} + {y} ={result}')
        except ValueError:
            tries -= 1
            print('EEE')
            user_result=input(f'{x} + {y }=')
            if tries==0:
                print(f'{x} + {y} = {result}')
                pass
    print('Score:',score)


def get_level():
    while True:
        try:
            n=int(input('Level: '))
            if n in range(1,4):
                return n
        except ValueError:pass




def generate_integer(level):
    if level==1:
        return random.randint(0, 9)
    elif level==2:
        return random.randint(10, 99)
    elif level==3:
        return random.randint(100, 999)




if __name__ == "__main__":
    main()