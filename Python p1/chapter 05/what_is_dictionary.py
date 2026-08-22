  # A dictionary is an unordered and mutable collection in Python that
# stores data in key–value pairs and uses keys instead of indexes to
# access values.

data = {
    "name": "moiz",
    "rollno": 14,
    "department": "computer science",
    "university": "University of Gujrat",
    "contactinfo": "+314-47******",
    777: "Mirxa g",
    "lixt": (3, 5, 5, 6),
}

print(data)
print(type(data))
print(data["university"])
print(data["contactinfo"])
print(data[777])
print(data["lixt"])

# how to make empty dictionary
data = {}
print(type(data))
