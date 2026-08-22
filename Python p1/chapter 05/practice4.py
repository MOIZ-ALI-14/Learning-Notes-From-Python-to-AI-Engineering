# Note:
# In a dictionary, each key must be unique.
# If a student name (key) is entered again with a new language (value),
# the old language will be replaced with the new one.
# Example:
# Moiz → English
# Junaid → Urdu
# Junaid → spanish  (previous Urdu is replaced by spanish)
# The dictionary will not have a "third Junaid" entry; update() just replaces the value.

liking = {}

name = input("enter your name: ")
lang = input("enter your favourite language: ")
liking.update({name: lang})
name = input("enter your name: ")
lang = input("enter your favourite language: ")
liking.update({name: lang})
name = input("enter your name: ")
lang = input("enter your favourite language: ")
liking.update({name: lang})

print(liking)
