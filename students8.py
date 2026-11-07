import csv

ism = input("Ismni kiriting: ")
yosh = input("Yoshni kiriting: ")
kurs = input("Kursni kiriting: ")

with open('students.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow([ism, yosh, kurs])

print("\nYangi o'quvchi qo'shildi. Yangilangan ro'yxat:")
with open('students.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(", ".join(row))