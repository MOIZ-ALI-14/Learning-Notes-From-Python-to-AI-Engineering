with open("chapter 09/13_CopyFile.txt", "r") as f:
    content1 = f.read()
with open("chapter 09/13_file.txt", "r") as f:
    content2 = f.read()

if content1 == content2:
    print("Yes! these files are identical")
else:
    print("No! these files are not identical")
