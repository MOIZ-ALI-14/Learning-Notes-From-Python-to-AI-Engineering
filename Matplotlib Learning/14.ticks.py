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
plt.xticks([1, 2, 3, 4, 5], ["M1", "M2", "M3", "M4", "M5"])
plt.yticks([0, 1000, 2000, 3000], ["0", "1K", "2K", "3K"])
plt.show()


# X-ticks and Y-ticks control the positions and labels displayed on the graph axes.
# We can use custom labels to make the tick values easier to understand.
# xticks() controls the X-axis ticks, while yticks() controls the Y-axis ticks.
# Example: we can show "M1", "M2" for months or "1K", "2K" for sales values.


# plt.show() displays the completed graph on the screen.
# It is usually placed at the end after all graph settings are applied.
