
Menu={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00 }
Total=0.00
def main():
    while True:
        try:
            item = input('Item: ').title()
            print(f'Total: ${GetTotal(item):.2f}')
        except EOFError:
            print()
            break
        except (KeyError,TypeError):
            pass
def GetTotal(s):
    global Total
    if s in Menu:
        Total=Menu[s]+Total
        return Total




main()