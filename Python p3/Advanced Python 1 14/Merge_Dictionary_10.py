# | pipe operator can also MERGE two dictionaries together
# WHAT: | between two dictionaries combines them into one dictionary
# WHEN: Use when you want to join two dictionaries into single one
# NOTE: If both dictionaries have same key - second dictionary value wins

dict1 = {"Apple": 5, "Mango": 3}
dict2 = {"Guava": 4, "Mango": 6}
combined_Dict = dict1 | dict2
print(combined_Dict)
