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
plt.show()


# A title gives the graph a clear name and tells us what the data represents.
# Example: plt.title() adds "Monthly Sales Data Report" at the top of the graph.
