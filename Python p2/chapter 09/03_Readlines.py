# readlines() - reads the ENTIRE file and returns a LIST
# each line in the file becomes a separate item in the list
# example output: ['Hello\n', 'My name is Mirxa\n', 'I am learning
#  Python']
f = open("chapter 09/03_File.txt", "r")
print(f.readlines())
print(type(f.readlines()))
f.close()
