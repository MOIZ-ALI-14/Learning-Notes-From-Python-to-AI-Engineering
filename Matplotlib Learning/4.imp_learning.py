# A data point is one piece of information represented by an X-value and its corresponding Y-value.
# X usually represents the input, while Y represents the output or result for that input.
# Example: (2, 10) means when X = 2, the corresponding Y = 10.


# X-axis is the horizontal line of a graph, usually used to show input or independent values.
# Y-axis is the vertical line of a graph, usually used to show output or dependent values.
# Example: In study hours vs marks, X-axis = study hours and Y-axis = marks.


# A figure is the complete area or window where our graph or visualization is placed.
# It can contain one or more graphs and can be customized in size and layout.
# Example: One figure can contain a sales graph and a profit graph together.


# Axes are the actual area inside a figure where we draw and view the graph.
# They contain the X-axis, Y-axis, data points, labels, and other graph elements.
# Example: A figure can have two axes, one for sales and another for profit.


# A plot is the visual representation of data on a graph.
# It takes our data points and shows them using lines, bars, points, etc.
# Example: plt.plot(x, y) plots the values of y according to their x-values.


# A marker is a symbol used to show individual data points on a graph.
# We can choose different markers like circle, square, star, or triangle.
# Example: plt.plot(x, y, marker='o') shows each data point as a circle.


# Line style controls the appearance of the line connecting data points.
# We can use styles like solid, dashed, dotted, or dash-dot.
# Example: plt.plot(x, y, linestyle='--') creates a dashed line.


# Color is used to change the color of the line or other graph elements.
# We can use common colors like red, blue, green, and black.
# Example: plt.plot(x, y, color='red') creates a red line.


# A legend tells us what each line, marker, or data series represents.
# It is useful when a graph contains multiple data series.
# Example: plt.legend() displays the labels given to each plotted line.


# A label gives a name or description to a part of the graph, such as the X-axis or Y-axis.
# Labels make the graph easier to understand and explain what the data represents.
# Example: plt.xlabel("Months") gives the X-axis the label "Months".


# A title gives the graph a clear name and tells us what the graph represents.
# It helps the viewer understand the purpose of the graph at a glance.
# Example: plt.title("Monthly Sales") adds "Monthly Sales" as the graph title.


# A grid adds horizontal and vertical lines to the graph to make values easier to read.
# It helps us compare data points with the X-axis and Y-axis values.
# Example: plt.grid() displays a grid on the graph.


# DPI (dots per inch) controls the resolution or sharpness of a figure.
# Higher DPI makes the saved or displayed figure more detailed and clearer.
# Example: plt.figure(dpi=150) creates a figure with 150 DPI.


# A backend is the part of Matplotlib that handles how a graph is displayed or saved.
# It connects Matplotlib with the screen, notebook, or image file.
# Example: a backend can display a graph in a window or save it as a PNG file.
