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
plt.xlim(1, 6)
plt.ylim(0, 3000)
plt.show()


# xlim() and ylim() control the visible range of the X-axis and Y-axis.
# They are useful when we want to focus the graph on a specific range of values.
