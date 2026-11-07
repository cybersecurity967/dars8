import csv

sportchilar = []
with open('sportchilar.csv', 'r') as f:
    reader = csv.DictReader(f)
    print("Barcha sportchilar:")
    for row in reader:
        sportchilar.append({
            'ism': row['ism'],
            'sport': row['sport'],
            'ball': int(row['ball'])
        })
        print(f"{row['ism']} ({row['sport']}) - {row['ball']} ball")

print("\n80 balldan yuqori natija olgan sportchilar:")
for s in sportchilar:
    if s['ball'] > 80:
        print(f"{s['ism']} — {s['ball']} ball")

eng_yuqori = max(sportchilar, key=lambda x: x['ball'])
print(f"\nEng yuqori ball olgan sportchi: {eng_yuqori['ism']} ({eng_yuqori['sport']}) - {eng_yuqori['ball']} ball")