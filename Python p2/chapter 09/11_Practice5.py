with open("chapter 09/11_File.txt", "r") as f:
    content = f.read()
    if "Python" in content:
        print("Python is present")
    else:
        print("Python is not present")
