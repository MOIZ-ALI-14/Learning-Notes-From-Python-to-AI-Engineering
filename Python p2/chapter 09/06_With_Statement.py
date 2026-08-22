# with statement - the SMART way to open files in Python
# it automatically closes the file when the block ends
# you don't need to write f.close() manually ever again!
# lets use with statement for read , just to understand that
# with statement will safe us from writing close()

with open("chapter 09/06_File.txt", "r") as f:
    print(f.read())
    print(type(f.read()))
