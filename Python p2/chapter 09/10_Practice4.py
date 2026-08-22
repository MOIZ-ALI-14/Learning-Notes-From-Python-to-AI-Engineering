data = ["Hamza", "Moiz", "Murtaza"]
with open("chapter 09/10_File.txt", "r") as f:
    content = f.read()
    for data_item in data:
        content = content.replace(data_item, "Junaid")

with open("chapter 09/10_File.txt", "w") as f:
    f.write(content)
