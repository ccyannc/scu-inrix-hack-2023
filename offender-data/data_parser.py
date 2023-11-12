import json

with open("sex_offender_raw_data.txt", "r") as f1:
    raw = f1.read()

json_obj = json.loads(raw)

total = 0
actual = 0

f2 = open("sex_offender_parsed.txt", "w")


for item in json_obj["d"]["Offenders"]:
    lat = item["Latitude"] 
    long = item["Longitude"]

    if (lat != 0.0 and long != 0.0):
        f2.writelines(str([lat, long]))
        f2.writelines("\n")
        print([lat, long])
        actual += 1

    
    total += 1

    
print(actual)
print(total)