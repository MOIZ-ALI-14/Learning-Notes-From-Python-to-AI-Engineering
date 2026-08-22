# append mode "a" - opens file and adds content at the END
# it does NOT delete/overwrite existing content
# if file does NOT exist, Python will CREATE it automatically
data = "Hardworking Student i am Moiz"
f = open("chapter 09/05_File.txt", "a")
f.write(data)
f.close()
# IMPORTANT NOTES:
# "a" will NEVER delete your existing data   --> SAFE
# "w" will DELETE all existing data          --> DANGEROUS
# always use "a" when you want to ADD data
# always use "r" when you want to READ data
# always use "w" only when you want FRESH start

# MODES SUMMARY:
# "r"  --> read only
# "w"  --> write  (deletes old content)
# "a"  --> append (keeps old content, adds at end)
