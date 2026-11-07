import json

talaba = {
    "ism": "Sardor",
    "yosh": 20,
    "kurs": 2
}

json_matn = json.dumps(talaba, ensure_ascii=False, indent=4)
print("JSON matn:")
print(json_matn)

qayta_dict = json.loads(json_matn)
print(f"\nTalabaning ismi: {qayta_dict['ism']}")