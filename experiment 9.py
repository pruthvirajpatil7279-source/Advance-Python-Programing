import csv
import json
import os

# Folder where this script is saved
base = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base, "input.csv")
json_path = os.path.join(base, "output.json")

# Create input.csv if it does not exist
if not os.path.exists(csv_path):
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        f.write("name,branch,year,cgpa\n")
        f.write("Nikhil,COE,2,9.0\n")
        f.write("Sanchit,COE,2,9.1\n")
        f.write("Aditya,IT,2,9.3\n")
        f.write("Sagar,SE,1,9.5\n")

# Read the CSV file and convert each row into a dictionary
data = []
with open(csv_path, "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

print("Number of records read:", len(data))

# Write the list of dictionaries to a JSON file
with open(json_path, "w", encoding="utf-8") as jsonfile:
    json.dump(data, jsonfile, indent=4)

print("Data written to output.json")
print(json.dumps(data, indent=4))