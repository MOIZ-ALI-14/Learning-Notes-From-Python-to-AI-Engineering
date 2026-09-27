import matplotlib.pyplot as plt

classes = ["9th", "10th", "11th", "12th"]

marks1 = [90, 100, 83, 96]
marks2 = [85, 92, 88, 95]
marks3 = [78, 89, 94, 98]

# Create one Figure and three Axes
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

# ---------------- Chart 1 ----------------
ax1.plot(classes, marks1, marker="o", color="blue")
ax1.set_title("Student A")
ax1.set_xlabel("Classes")
ax1.set_ylabel("Percentage")
ax1.grid()

# ---------------- Chart 2 ----------------
ax2.plot(classes, marks2, marker="s", color="green")
ax2.set_title("Student B")
ax2.set_xlabel("Classes")
ax2.set_ylabel("Percentage")
ax2.grid()

# ---------------- Chart 3 ----------------
ax3.plot(classes, marks3, marker="^", color="red")
ax3.set_title("Student C")
ax3.set_xlabel("Classes")
ax3.set_ylabel("Percentage")
ax3.grid()

# adding a main title to complete figure, above all subplots
plt.suptitle("Different Charts for Learning")

# Adjust spacing between charts
plt.tight_layout()

# Display the complete Figure
plt.show()


# Object-Oriented API is useful when a project has multiple charts that need separate control.
# We create one Figure (fig) and three Axes (ax1, ax2, ax3) using plt.subplots(3, 1).
# The 3, 1 means 3 rows and 1 column, so three charts are arranged vertically.
# Each Axes object controls its own chart, so we can set its title, labels, grid, and data separately.
# ax1, ax2, and ax3 are just variable names; we can choose other names if we want.
# We use ax.plot() instead of plt.plot() because we are directly controlling a specific Axes object.
# plt.tight_layout() automatically adjusts the spacing so titles and labels do not overlap.
# This approach keeps large projects organized because each chart can be tracked and managed independently.
