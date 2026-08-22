name = input("enter your name dear: ")
print(f"Good Afternoon! {name}")  # f means using fstring

date = input("enter today's date dear: ")
print(f"Dear <{name}> \n You are selected! \n {date}")

# detecting double space and replacing it in a string
newline = "Moiz Ali is very  honest  boy"
print(newline.find("  "))
updated_string = newline.replace("  ", " ")
print(updated_string)
print(newline)
