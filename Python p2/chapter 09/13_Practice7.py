with open("chapter 09/13_file.txt", "r") as f:
    content = f.read()

with open("chapter 09/13_CopyFile.txt", "w") as f:
    f.write(content)
