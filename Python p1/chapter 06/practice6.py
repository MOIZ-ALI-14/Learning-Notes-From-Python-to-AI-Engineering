# We use the lower() method so that if the user enters "Moiz", "MOIZ",
# or any uppercase/lowercase variation, it will be converted to lowercase.
# This allows us to detect the word correctly using the 'in' keyword.

comment = input("enter your comment: ")
if "moiz" in comment.lower():
    print("this comment is related to moiz")
else:
    print("this comment is not related to moiz")
