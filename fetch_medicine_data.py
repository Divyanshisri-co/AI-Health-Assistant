import requests
import json

url = "https://api.fda.gov/drug/label.json?limit=20"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print("Error fetching data")
    exit()

medicines = {}

for item in data['results']:
    try:
        name = item.get('openfda', {}).get('brand_name', ["Unknown"])[0]

        use = item.get('indications_and_usage', ["No info available"])[0]

        precaution = item.get('warnings', ["No precautions available"])[0]

        medicines[name.lower()] = {
            "name": name,
            "use": use[:200],          # limit text length
            "precaution": precaution[:200]
        }

    except:
        continue

# Save JSON
with open("data/medicine.json", "w") as f:
    json.dump(medicines, f, indent=4)

print("Dataset created successfully!")