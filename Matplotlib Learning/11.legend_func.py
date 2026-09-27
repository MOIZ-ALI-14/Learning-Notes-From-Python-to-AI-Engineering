import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]

sales = [1123, 2322, 1220, 432, 3002]
profit = [500, 900, 700, 300, 1200]

plt.plot(
    months,
    sales,
    color="green",
    marker="s",
    label="Sales",
)

plt.plot(
    months,
    profit,
    color="blue",
    marker="o",
    label="Profit",
)

plt.xlabel("Months")
plt.ylabel("Amount")
plt.title("Monthly Sales and Profit")

plt.legend(loc="upper left", fontsize="10", title="Data", frameon="True")

plt.show()


# plt.legend() displays the labels of the plotted data on the graph.
# loc controls where the legend appears, such as "upper left" or "lower right".
# fontsize controls the size of the text inside the legend.
# title adds a heading to the legend to make it more descriptive.
# frameon controls whether a box is shown around the legend.
# The legend appears with useful names only when we provide a label while plotting the data.
