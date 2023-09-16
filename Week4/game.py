import random
import sys
def main():
    while True:
        try:
            n=int(input('Level:'))
            if n>0:Checkguess(n)
        except ValueError:
            pass
def Checkguess(n):
    while True:
        try:
            number = random.randint(1, n)
            guess=int(input('Guess:'))
            if guess in range(1,n+1):
                if guess>number:
                    print('Too large!')
                elif guess<number:
                    print('Too small!')
                elif guess==number:
                    print('Just right!')
                    sys.exit()
        except ValueError:
            pass
main()