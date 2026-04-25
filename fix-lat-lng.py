import json

with open('/home/xiaobai/storage/footprint/data.json', 'r') as f:
    d = json.load(f)

for dest in d['destinations']:
    lat_val = dest.pop('lat')
    lng_val = dest.pop('lng')
    dest['lng'] = lat_val
    dest['lat'] = lng_val

with open('/home/xiaobai/storage/footprint/data.json', 'w') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

# Verify
for dest in d['destinations']:
    print(f"{dest['name']}: lat={dest['lat']}, lng={dest['lng']}")
