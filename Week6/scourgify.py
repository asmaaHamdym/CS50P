import sys
import csv
students=[]
try:
    if len(sys.argv)<= 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3:
        if not sys.argv[1].endswith(".csv"):
            sys.exit(f"Could not read {sys.argv[1]}")
        elif not sys.argv[2].endswith(".csv"):
            sys.exit(f"Could not read {sys.argv[2]}")

        else:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append({"name": row["name"], "house": row["house"]})

            with open(sys.argv[2],'w') as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for student in students:
                    last,first=student['name'].split(',')
                    writer.writerow({"first":first.strip() ,"last":last.strip() , "house": student['house']})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")