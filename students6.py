import csv

with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)
    print("Barcha o'quvchilar:")
    for row in reader:
        print(row['ism'])

with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)
    print("\n20 yoshdan katta o'quvchilar:")
    for row in reader:
        if int(row['yosh']) > 20:
            print(f"{row['ism']} — {row['yosh']} yosh")