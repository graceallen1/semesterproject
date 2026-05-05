#!/usr/bin/env python3
import urllib.request, urllib.parse, json, time, sys, os
places = [
    ("Press Cafe", "4801 Edwards Ranch Rd, Fort Worth, TX"),
    ("Eatzi's Market & Bakery", "1540 S University Dr, Fort Worth, TX"),
    ("Paloma Suerte", "122 E Exchange Ave, Fort Worth, TX"),
    ("Hudson House", "4600 Dexter Ave, Fort Worth, TX"),
    ("Woodshed Smokehouse", "3201 Riverfront Dr, Fort Worth, TX"),
    ("Quince Riverside", "1701 River Run, Fort Worth, TX"),
    ("Joe T. Garcia's", "2201 N Commerce St, Fort Worth, TX"),
    ("Heim Barbecue", "1109 W Magnolia Ave, Fort Worth, TX"),
    ("Local Foods", "1617 Park Place Ave, Fort Worth, TX"),
    ("Pacific Table", "1600 S University Dr, Fort Worth, TX"),
    ("Maggie's R&R", "212 S Main St, Fort Worth, TX"),
    ("HG Sply Co.", "1621 River Run, Fort Worth, TX"),
    ("Coco Shrimp", "3000 Crockett St, Fort Worth, TX"),
    ("Oishii Sushi", "2700 W 7th St, Fort Worth, TX"),
    ("Pie Tap Pizza Workshop + Bar", "2400 W 7th St, Fort Worth, TX"),
    ("Bricks and Horses", "Fort Worth, TX"),
    ("Hotel Drover Restaurant", "200 Mule Alley Dr, Fort Worth, TX"),
    ("Lucile’s", "4700 Camp Bowie Blvd, Fort Worth, TX"),
    ("Doc B's", "5252 Monahans Ave, Fort Worth, TX")
]

out_lines = ["Name,Address,Lat,Lon"]
for name, addr in places:
    query = urllib.parse.quote(addr + ", Fort Worth, TX")
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={query}&limit=1"
    req = urllib.request.Request(url, headers={"User-Agent": "semesterproject-graceallen/1.0 (contact: graceallen@example.com)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.load(resp)
            if data:
                lat = data[0].get('lat')
                lon = data[0].get('lon')
                out_lines.append(f'"{name}","{addr}",{lat},{lon}')
                print(f'{name}: {lat},{lon}')
            else:
                out_lines.append(f'"{name}","{addr}",,')
                print(f'{name}: NOT FOUND')
    except Exception as e:
        out_lines.append(f'"{name}","{addr}",,')
        print(f'{name}: ERROR: {e}', file=sys.stderr)
    time.sleep(1)

out_path = os.path.join(os.path.dirname(__file__), '..', 'food_coords.csv')
with open(out_path, 'w') as f:
    f.write('\n'.join(out_lines))
print('\nWrote', out_path)
