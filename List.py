# List Indexing Examples

# Create a sample list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive Indexing (from the beginning)
print(fruits[0])   # Output: apple
print(fruits[2])   # Output: cherry
print(fruits[4])   # Output: elderberry

# Negative Indexing (from the end)
print(fruits[-1])  # Output: elderberry
print(fruits[-2])  # Output: date
print(fruits[-5])  # Output: apple

# Slicing
print(fruits[1:4])      # Output: ['banana', 'cherry', 'date']
print(fruits[:3])       # Output: ['apple', 'banana', 'cherry']
print(fruits[2:])       # Output: ['cherry', 'date', 'elderberry']
print(fruits[::2])      # Output: ['apple', 'cherry', 'elderberry']
print(fruits[::-1])     # Output: ['elderberry', 'date', 'cherry', 'banana', 'apple']

# Modifying elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

# Common list methods
print(len(fruits))          # Length of list
print("cherry" in fruits)   # Check if element exists
print(fruits.index("date")) # Find index of element