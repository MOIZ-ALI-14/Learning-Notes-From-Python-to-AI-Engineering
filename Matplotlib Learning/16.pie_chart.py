import matplotlib.pyplot as plt

revenue = [12000, 55000, 9900, 35000]
provinces = ["Sindh", "Punjab", "KpK", "Balochistan"]
plt.pie(
    revenue,
    labels=provinces,
    autopct="%1.1f%%",
    explode=[0, 0, 0.3, 0],
    shadow=True,
    startangle=90,
    wedgeprops={"edgecolor": "black", "linewidth": 1},
    colors=["red", "green", "blue", "yellow"],
    textprops={"fontsize": 11},
    pctdistance=0.7,
    labeldistance=1.1,
)
plt.title("Revenue Contribution by Provinces")
plt.show()


# A pie chart is used to show how different categories contribute to one complete total.
# Use it when the data represents percentages, proportions, or shares of a whole.
# It works best with a small number of categories, usually around 3–6, so the slices remain easy to compare.
# labels names each slice, while colors can be used to visually distinguish the categories.
# autopct displays the percentage of each slice directly on the pie chart.
# "%1.1f%%" means show the percentage as a floating-point number with 1 digit after the decimal, followed by the % sign.
# Example: 25.678% is displayed as 25.7%;


# explode separates the slice we want to highlight.
# shadow adds a shadow behind the pie chart.
# startangle rotates the entire pie chart for better positioning.
# wedgeprops controls the edges of the slices, such as color and thickness.
# textprops customizes the appearance of text.
# pctdistance controls the position of percentage values.
# labeldistance controls the position of category labels.
