import sys
try:
    count=0
    if len(sys.argv)==1 :
        sys.exit('too few command-line arguments')
    elif  not sys.argv[1].endswith('.py') and len(sys.argv)==2:
        sys.exit('Not a Python file')
    elif len(sys.argv)>2:
        sys.exit('too many command;line arguments')
    elif len(sys.argv)==2:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
        for line in lines:
            if line.lstrip().startswith('#') or line.isspace(): continue
            else: count+=1
        print(count)

except FileNotFoundError:
    sys.exit('File does not exist')