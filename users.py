import json

with open('user.json', 'r') as f:
    data = json.load(f)

print(f"Ism: {data['ism']}")
print(f"Yosh: {data['yosh']}")
print(f"Shahar: {data['shahar']}")