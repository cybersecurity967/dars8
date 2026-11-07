import json
with open('product.json', 'r') as f:
    data = json.load(f)

umumiy_qiymat = data['narx'] * data['miqdor']

print(f"Mahsulot: {data['nom']}")
print(f"Umumiy qiymat: {umumiy_qiymat}")