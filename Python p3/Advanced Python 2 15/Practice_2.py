# str(...)   = converts result to string - because join() only accepts
#              strings - without str() join() would give TypeError
table = [str(3 * i) for i in range(1, 11)]
print("\n".join(table))
