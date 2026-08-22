# It will give length 2 instead of 3 because 30 (int) and 30.0 (float) are considered
# equal in Python sets.
# "30" (string) is different, so it is added separately.

s = set()
s.add(30)
s.add(30.0)
s.add("30")
print(s)
print(len(s))
