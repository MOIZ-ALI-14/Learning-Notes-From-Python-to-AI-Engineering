try:
    with open("file1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("Advanced Python 1 14/Practice_1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("file3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thank YOu")
