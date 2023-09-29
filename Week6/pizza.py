import sys
import csv
from tabulate import tabulate

menu=[]
try:

    if  len(sys.argv)==1:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv)>2:
        sys.exit('Too many command-line arguments')
    elif  not sys.argv[1].endswith('.csv'):
        sys.exit('Not a CSV file')
    elif len(sys.argv)==2:
        with open(sys.argv[1]) as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                menu.append(row)

        print(tabulate(menu, headers='firstrow', tablefmt="grid"))





except FileNotFoundError:
    sys.exit('File does not exist')