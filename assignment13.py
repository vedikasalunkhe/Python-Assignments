import json
import csv

def json_to_csv(json_file, csv_file):
    try:
        with open(json_file, "r") as jf:
            data = json.load(jf)

        # Assuming JSON array of dictionaries
        with open(csv_file, "w", newline="") as cf:
            writer = csv.DictWriter(cf, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        print("Conversion successful!")
    except Exception as e:
        print("Error:", e)

# Example usage
json_to_csv("data.json", "output.csv")