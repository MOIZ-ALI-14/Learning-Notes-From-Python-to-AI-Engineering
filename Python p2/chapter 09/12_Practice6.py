with open("chapter 09/12_File.txt", "r") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if "Python" in line:
        print(f"Python is Present, Line no {lineNo}")
        break
    lineNo = lineNo + 1
else:
    print("Python is not present!")
