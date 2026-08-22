# A dictionary is an unordered and mutable collection in Python that
# stores data in key–value pairs and uses keys instead of indexes to
# access values.

data = {
    "name": "moiz",
    "rollno": 14,
    "contactinfo": "+314-47******",
    "lixt": (3, 5, 5, 6),
}

print(data.items())  # returns a list of (key,value) as a tuple
print(data.keys())  # returns a list of keys in a dictionary as a tuple
print(data.values())  # returns a list of values in a dictionary as a tuple
data.update(
    {"name": "Moiz_Ali", "Section": "B"}
)  # it will update the existed item in the original dictionary and will add more items also
print(data)
print(len(data))  # it will print the length of the dictionary

# these both lines will print Moiz_Ali but difference is that get method
# returns none if item doesn't exist and the simple method gives error if
# itme doesn't exist
print(data.get("name"))
print(data["name"])

# pop method will remove the key-value pair whom key we will provide
# it will also return the deleted value
deletedvalue = data.pop("contactinfo")
print(deletedvalue)
print(data)

# pop-item method will remove the last inserted key-value pair in dictionary
# it doesn't requird the key from us as pop method required
# it will also return the deleted key-value pair as a tuple
print(data.popitem())
print(data)
