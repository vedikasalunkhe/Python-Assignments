
# Make Normal Dictionary
Result = {
    "Name" : "Mahesh Saste",
    "Subject Marks" : {
        "Physics" : 84,
        "Chemistry" : 64,
        "Maths" : 75
    }
}

# .key Method
# for printing keys
print(Result.keys())

# List of keys
print(list(Result.keys()))

# .values Method
# printing values under the keys
print(Result.values())

# printing list of values under the keys
print(list(Result.values()))

# measuring length of values under the keys
print(len(Result.values()))

# .items Method
# Printing all info given in  Dict in Tuple Form = ()
print(Result.items())

# printing list of info given in  Dict in Tuple Form = ()
print(list(Result.items()))

# .get Method
# name2 is not available in our dict > shows error
# we have used .get > no error we will show > Shows : None
info = {
    "name": "mahesh",
}

print(info.get("name2"))

# .update Method
# Adds Any Key
Result.update({"City" : "Pune"})
print(Result)