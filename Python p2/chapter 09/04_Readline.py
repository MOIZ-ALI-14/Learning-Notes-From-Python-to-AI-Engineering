# readline() - reads ONE line at a time, returns a STRING
# every time you call readline() it moves to the NEXT line
f = open("chapter 09/04_File.txt", "r")
# simple method
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# Now, using while loop
line = f.readline()
while line != "":
    print(line)
    line = f.readline()
print(type(line))
f.close()
