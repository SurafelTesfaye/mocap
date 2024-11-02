# Need to properly check if it is 10*10


import matplotlib.pyplot as plt
import numpy as np

# Set the figure size
plt.figure(figsize=(10, 10))

# Draw the grid lines
for x in np.arange(0, 11, 1):  # Vertical lines at each meter
    plt.axvline(x, color='lightgray', linewidth=1)
for y in np.arange(0, 11, 1):  # Horizontal lines at each meter
    plt.axhline(y, color='lightgray', linewidth=1)

# Add labels for axes (optional)
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(0, 11, 1))

# Set the axis limits to match the 10m x 10m space
plt.xlim(0, 10)
plt.ylim(0, 10)

# Set labels and title
plt.xlabel('X (meters)')
plt.ylabel('Y (meters)')
plt.title('10m x 10m Vicon Lab Grid')

# Display the plot
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(False)  # Disable Matplotlib's default grid to show only custom grid lines
plt.show()
