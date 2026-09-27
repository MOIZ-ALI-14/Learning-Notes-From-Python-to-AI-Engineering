# pyplot is a module inside Matplotlib that provides ready-made plotting functions.
# It saves us from creating graphing tools from scratch.
# Like ready-made brushes for painting a wall, pyplot gives us ready-made tools for graphs.
# We commonly import it as: import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 13, 15, 25, 5]
plt.plot(x, y)
plt.show()
# x and y contain the points we want to plot; each x value is matched with its y value.
# plt.plot(x, y) creates the line graph, and plt.show() displays it on the screen.
