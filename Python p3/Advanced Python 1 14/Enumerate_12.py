# ENUMERATE - COMPLETE REFERENCE
# ================================
# WHAT: enumerate gives both index and value of list together
# WHY:  Without enumerate you need separate index variable
#       and manually increment it - lengthy and messy code
# WHEN: Use when you need both index and value in a loop
# HOW:  for index, item in enumerate(list)

# To prevent this lengthy code
# L = [3, 33, 32, 54, 6545]
# index = 0
# for item in L:
#     print(f"The numbre at index {index} is {item}")
#     index += 1

# we do this
L = [3, 33, 32, 54, 6545]
for index, item in enumerate(L):
    print(f"The number at index {index} is {item}")
