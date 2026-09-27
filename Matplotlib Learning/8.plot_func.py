import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
sales = [1123, 2322, 1220, 432, 3002]
plt.plot(
    months,
    sales,
    color="green",
    linestyle="--",
    linewidth=2,
    marker="s",
    label="sales per month",
)
plt.show()

# plt.plot() is mainly used to show data points and connect them to visualize a trend or relationship.
# It is commonly used for line charts, especially when we want to see how values change over time.
# Here, months are on the X-axis and sales are on the Y-axis, so we can see the monthly sales trend.
# color, linestyle, linewidth, and marker customize how the plotted data looks; these are optional.
# label="sales per month" gives the plotted line a name, but it will not appear unless we use plt.legend().
# Real-life example: plt.plot() can show how a company's sales, temperature, or website visitors change over time.
