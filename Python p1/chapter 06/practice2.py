math_marks = int(input("enter marks of math: "))
phy_marks = int(input("enter marks of physics: "))
CS_marks = int(input("enter marks of computer science: "))

total_perc = (100 * (math_marks + phy_marks + CS_marks)) / 300
math_perc = math_marks
phy_perc = phy_marks
CS_perc = CS_marks

if (math_perc >= 33 and phy_perc >= 33 and CS_perc >= 33) and total_perc >= 40:
    print(f"Congratulations! you have passed with the percentage {total_perc}")
else:
    print("you have failed")
