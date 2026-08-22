with open("chapter 09/09_File.txt", "r") as f:
    content = f.read()
    new_content = content.replace("Wolfee", "haha")

with open("chapter 09/09_File.txt", "w") as f:
    f.write(new_content)
