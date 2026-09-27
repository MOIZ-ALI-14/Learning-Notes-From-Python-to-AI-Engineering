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
plt.title("Monthly Sales Data Report")
plt.grid(color="red", linestyle=":", linewidth="1")
plt.show()

# A grid adds horizontal and vertical reference lines to make graph values easier to read.
# We can customize its color, line style, and width according to our preference.
# Example: plt.grid(color="red", linestyle=":", linewidth=1) creates a red dotted grid.
# The grid is optional and can be skipped when the graph is already easy to read.
