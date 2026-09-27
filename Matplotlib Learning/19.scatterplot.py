import matplotlib.pyplot as plt

study_hrs = [1, 2, 3, 4, 5, 6]
sec_A_marks = [60, 65, 78, 90, 95, 98]
sec_B_marks = [45, 49, 54, 60, 71, 75]
plt.scatter(study_hrs, sec_A_marks, color="green", marker="*", label="Section A Marks")
plt.scatter(study_hrs, sec_B_marks, color="orange", marker="^", label="Section B Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scored")
plt.title("Comparison of Two Sections")
plt.legend()
plt.grid()
plt.show()


# Scatter plot is used to show the relationship between two numerical variables.
# It represents data using separate points instead of bars or lines.
# We use it to see whether one variable changes when another variable changes.
# It helps us easily find patterns, trends, or relationships in the data.
# It is commonly used in data analysis, statistics, and machine learning.
# For example, we can see whether more study hours are related to higher exam marks.
# Each point represents one pair of values, such as study hours and marks.

# color (or c) -> changes the color of the points.
# label -> gives a name to the plotted data, which appears when plt.legend() is used.
# marker -> changes the shape of the points, such as 'o', 'x', '^', or '*'.
# s -> controls the size of the points.
# alpha -> controls the transparency of the points (0 = transparent, 1 = fully visible).
# edgecolors -> changes the color of the boundary/edge around each point.
# linewidths -> controls the thickness of the point's edge.


# If one variable changes and the other tends to change, we say they may be related/correlated.
# If study hours increase and marks tend to increase, that's a positive correlation.
# If study hours increase and marks tend to decrease, that's a negative correlation.
# If one changes but the other shows no consistent pattern, there may be little or no correlation.


# In this example, study hours and exam marks are the two numerical variables.
# Study hours are on the x-axis, while exam marks are on the y-axis.
# Section A and Section B are two different groups being compared.
# We use two scatter plots to see the relationship between study hours and marks in each group.
