with open("chapter 09/07_File.txt", "r") as f:
    content = f.read()
    if "Gujrat" in content:
        print("Gujrat is present in the File")
    else:
        print("Gujrat is not present in the File")
