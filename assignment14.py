filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected error:", e)