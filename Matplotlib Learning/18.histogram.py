import matplotlib.pyplot as plt

scores = [
    22,
    53,
    56,
    64,
    45,
    22,
    53,
    77,
    76,
    84,
    93,
    33,
    54,
    58,
    65,
    23,
    66,
    99,
    23,
    53,
    61,
    71,
]
plt.hist(
    scores,
    bins=6,  # Divides the numerical data into 6 ranges.
    color="green",  # Sets the color of the histogram bars.
    edgecolor="black",  # Sets the color of the borders around the bars.
    linewidth=1,  # Controls the thickness of the bar borders.
    alpha=0.8,  # Controls the transparency of the histogram bars.
    label="Student Scores",  # Gives the histogram a name for the legend.
    rwidth=1,  # Controls the relative width of each histogram bar.
    density=False,  # Shows frequency/counts instead of probability density.
    histtype="bar",  # Sets the histogram style to normal bars.
    orientation="vertical",  # Makes the histogram bars extend vertically.
    align="mid",  # Aligns the bars around the center of their bin positions.
    cumulative=False,  # Shows the normal distribution instead of cumulative frequency.
    range=(20, 100),  # Sets the numerical range from 20 to 100 for the histogram.
    log=False,  # Keeps the Y-axis as a normal scale instead of logarithmic.
)
plt.title("Score Distribution of Students")
plt.xlabel("Score Ranges")
plt.ylabel("Number of Students")
plt.legend()
plt.show()


# A histogram is a graph used to show the distribution of numerical data.
# It divides continuous numerical values into different ranges called bins.
# We use it when we want to see how frequently values occur within each range.
# It helps us understand where most values are concentrated and how the data is spread.
# We use a histogram for data such as marks, ages, salaries, heights, temperatures, etc.
# Unlike a bar chart, histogram bars represent continuous numerical ranges and usually touch each other.
# A histogram is useful when our main goal is to understand the distribution and pattern of numerical data.


# bins=4 or bins=3 automatically divides the data range into the given number of bins.
# If we pass custom bin edges like [20, 30, 40, 50], we can define the exact ranges ourselves.
# This is useful when we want specific intervals such as 20–30, 30–40, and 40–50.
# The height of each bar shows how many values/students fall within that specific range.


# cumulative=True makes the histogram show cumulative frequency.
# Each bin includes the values counted in all previous bins.
# It is useful for seeing how many values fall below or within a certain range.
# Example: if bins have 10, 15, 20 students, the cumulative result becomes 10, 25, 45.
