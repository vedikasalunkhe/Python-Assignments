import csv

def count_rows(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            row_count = sum(1 for row in reader)
        print(f"Total number of rows: {row_count}")
    except FileNotFoundError:
        print("File not found.")

# Example usage
count_rows("data.csv")