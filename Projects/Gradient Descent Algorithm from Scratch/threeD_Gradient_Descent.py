import numpy as np
import matplotlib.pyplot as plt

def z_function(x, y):
  return np.sin(5 * x) * np.cos(5 * y) / 5

def calculate_gradient(x, y):
  return np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * x) * np.sin(5 * y)


x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)

Z = z_function(X, Y)

ax = plt.subplot(projection="3d")
ax.plot_surface(X, Y, Z, cmap="viridis")

plt.show()