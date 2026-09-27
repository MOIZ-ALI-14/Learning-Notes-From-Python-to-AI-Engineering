import matplotlib.pyplot as plt

Fruits = ["Mango", "Guave", "Apple", "Banana"]
sales = [4000, 2000, 7500, 6000]

plt.bar(
    Fruits,
    sales,
    color="purple",
    width=0.5,
    edgecolor="black",
    alpha=0.5,
    label="2026 sales"
)

# plt.barh(Fruits, sales, color="purple", label="2026 sales")

plt.xlabel("Fruits")
plt.ylabel("Sales")
plt.title("Fruit Sales Comparison")
plt.legend()
plt.show()

# A bar chart is used to compare values across different categories, where each category has a separate bar.
# It is useful for categorical data such as fruit sales, product revenue, student marks, or monthly expenses.
# The height of each bar represents the value, making differences between categories easy to compare.
# plt.bar() creates vertical bars, while plt.barh() creates horizontal bars.
# We can customize bars using properties like color, width, edgecolor, alpha, and label.
# Bar charts are mainly useful when categories are separate rather than showing a continuous trend over time.
# Real-life example: comparing the sales of different products in a shop or the revenue of different departments.
