import csv

xarajatlar = []
with open('expenses.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        xarajatlar.append({
            'nom': row['nom'],
            'summa': int(row['summa'])
        })

jami_summa = sum(x['summa'] for x in xarajatlar)
eng_katta = max(xarajatlar, key=lambda x: x['summa'])
soni = len(xarajatlar)

print(f"Jami xarajatlar summasi: {jami_summa}")
print(f"Eng katta xarajat: {eng_katta['nom']} ({eng_katta['summa']} so'm)")
print(f"Xarajatlar soni: {soni}")