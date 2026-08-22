c1 = "buy now"
c2 = "click this"
c3 = "subscribe this"
c4 = "make a lot of money"

line = input("enter your comment: ")
if c1 in line or c2 in line or c3 in line or c4 in line:
    print("this is a spam comment!")
else:
    print("yeah! you are valid")
