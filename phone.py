import json

# Faylni o'qish
with open('phone.json', 'r') as f:
    data = json.load(f)

print(f"Telefon modeli: {data['model']}")

yangi_narx = int(input("Yangi narxni kiriting: "))
data['narx'] = yangi_narx

with open('phone.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Telefon narxi muvaffaqiyatli yangilandi va saqlandi.")