import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
sales = [1123, 2322, 1220, 432, 3002]
plt.plot(
    months,
    sales,
    color="green",
    marker="s",
)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# Labels give names to the X-axis and Y-axis so we know what the data represents.
# Example: X-axis = Months and Y-axis = Sales.
