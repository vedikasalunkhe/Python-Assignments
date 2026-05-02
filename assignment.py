 File handling demonstration

# Writing to a file
file = open("example.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("This file demonstrates file handling.\n")
file.close()

# Reading the file
file = open("example.txt", "r")
content = file.read()
print("File Content after writing:")
print(content)
file.close()

# Appending to the file
file = open("example.txt", "a")
file.write("This line is appended later.\n")
file.close()

# Reading again after appending
file = open("example.txt", "r")
content = file.read()
print("\nFile Content after appending:")
print(content)
file.close()