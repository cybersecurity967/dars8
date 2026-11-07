import json

with open('student.json', 'r') as f:
    data = json.load(f)
data['ball'] = 95

with open('student.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("O'quvchining balli 95 ga o'zgartirildi va saqlandi.")