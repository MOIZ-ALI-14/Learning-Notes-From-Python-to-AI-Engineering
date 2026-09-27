import matplotlib.pyplot as plt

x = ["9th", "10th", "11th", "12th"]
y = [90, 100, 83, 96]
plt.plot(x, y)
plt.xlabel("Classes")
plt.ylabel("Perc of Marks")
plt.title("Marks Percentage in diff: Classes")
plt.savefig("Line_Chart.png", dpi=300, bbox_inches="tight")


# plt.savefig() saves the created chart as an image/file in the specified format.
# The file format is usually decided by the file extension, such as .png, .jpg, .pdf, or .svg.
# dpi (dots per inch) controls the resolution/quality of the saved image; higher dpi gives better quality.
# bbox_inches="tight" removes unnecessary empty space around the chart and keeps the figure neatly fitted.
