# WALRUS OPERATOR :=
# ===================
# WHAT: Walrus operator := assigns a value AND uses it at the same time
#       in a single line
# WHY:  Without walrus you have to write same variable twice
#       once for assignment and once for condition - repetition
# WHEN: Use inside while or if when you want to
#       assign and check condition at the same time
# HOW:  Put assignment inside parentheses with :=
#       (variable := value) then use condition after it

if (n := len([1, 3, 4, 5, 32, 33])) > 5:
    print(f"List is too long ({n} elements , expected <= 5)")

while (text := input("enter the text: ")) != "quit":
    print(text)
