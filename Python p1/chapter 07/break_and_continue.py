# The break statement is used to immediately stop the loop,
# even if the loop condition is still True.
# When break is executed, the loop terminates completely.
# In this program:
# The loop starts printing numbers from 0.
# When i becomes 4, the break statement stops the loop.
# So the output will be: 0, 1, 2, 3, 4
# The loop does not continue after 4.
for i in range(0, 33):
    print(i)
    if i == 4:
        break


# The continue statement is used to skip the current iteration
# and move to the next iteration of the loop.
# It does NOT stop the loop completely.
# In this program:
# "Moiz" is printed in every iteration.
# When i becomes 2, the continue statement skips the print(i) line.
# So when i == 2, only "Moiz" is printed, but 2 is not printed.
# The loop then continues normally until it finishes.
for i in range(0, 4):
    print("Moiz\t")
    if i == 2:
        continue
    print(i)


# use of pass
# The pass keyword is used as a placeholder.
# It does nothing and is used when a statement is required syntactically
# but you do not want to execute any code at that time.
# In the first loop, pass makes the loop run without producing any output.
data = [4, 4, 5, 6, 65]
for i in data:
    pass

data = [4, "moiz", 5, 6, 65]
for i in data:
    print(i)
