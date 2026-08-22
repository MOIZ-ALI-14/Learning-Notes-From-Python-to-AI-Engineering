# The else block with a for loop executes after the loop finishes normally.
# It runs only if the loop completes all iterations without encountering a break statement.
# In this program, the loop prints each element of the list one by one,
# and after printing all elements, the else block prints "Done!".

data = ["moiz", "junaid", "shabi", 4, 5, 64]
for i in data:
    print(i)
else:
    print("Done!")
