# Object-Oriented API is another way of working with Matplotlib.
# It is mainly useful when we are working on larger or more complex projects.
# Instead of controlling the graph mainly through pyplot,
# we create and work with specific objects such as Figure and Axes.
#
# A Figure represents the complete window or canvas of our visualization.
# An Axes represents the actual area where a graph is drawn.
# One Figure can contain multiple Axes, so we can create multiple charts
# inside the same figure and control each chart separately.
#
# This makes our code more organized and easier to manage.
# We can store each Figure or Axes in a variable and work with it directly.
# For example, we can create a Figure object and two Axes objects
# for showing two different charts in the same figure.
#
# Object-Oriented API is especially useful when a project has
# multiple charts, different layouts, or many custom settings.
# It gives us direct control over individual graphs and their properties.
# We can set titles, labels, grids, colors, limits, and other settings
# for each Axes object separately.
#
# Pyplot and Object-Oriented API can both create the same types of graphs.
# The main difference is how we control those graphs.
# Pyplot usually follows a state-based approach,
# where Matplotlib keeps track of the current Figure and Axes.
#
# Example with pyplot:
# plt.plot(x, y)
# plt.title("Sales")
# plt.xlabel("Month")
#
# In the Object-Oriented approach, we first create the objects:
# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title("Sales")
# ax.set_xlabel("Month")
#
# Here, ax directly represents the graph we want to control.
# This makes it easier to know exactly which chart we are modifying.
#
# Pyplot is simple and convenient for small graphs and quick visualizations.
# Object-Oriented API is more suitable for larger applications and projects.
# It also makes code easier to organize, maintain, and expand later.
#
# In short, pyplot focuses on the current graph,
# while Object-Oriented API lets us directly control specific graph objects.
