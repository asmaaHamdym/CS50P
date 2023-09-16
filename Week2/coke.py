Amount =50
coinList =[5,10,25]
print('Amount Due: ',50)

while 50>=Amount>0:
    coin =int(input('Insert Coin: '))
    if coin  in coinList:
         Amount = Amount-coin
    if Amount <=0:
        print('Change Owed',-Amount)
        break
    print('Amount Due: ',Amount)