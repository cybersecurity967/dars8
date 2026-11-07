import csv

mahsulotlar = []
with open('products.csv', 'r') as f:
    reader = csv.DictReader(f)
    print("Mahsulotlar va ularning umumiy qiymatlari:")
    for row in reader:
        narx = int(row['narx'])
        miqdor = int(row['miqdor'])
        umumiy = narx * miqdor
        mahsulotlar.append({'nom': row['nom'], 'narx': narx, 'umumiy': umumiy})
        print(f"{row['nom']}: {narx} x {miqdor} = {umumiy}")

eng_qimmat = max(mahsulotlar, key=lambda x: x['narx'])
print(f"\nEng qimmat mahsulot: {eng_qimmat['nom']} ({eng_qimmat['narx']} so'm)")