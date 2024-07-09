import numpy as np
import matplotlib.pyplot as plt


def y_function(x):
    return x ** 2


def y_derivative(x):
    return 2 * x  # The derivative of x^2 is 2x


# Generate values for plotting the function
X = np.arange(-5, 5, 0.1)
y = y_function(X)

# Initial position and learning rate
current_pos = 3.0
learning_rate = 0.01

# Gradient descent loop
for _ in range(500):
    new_x = current_pos - learning_rate * y_derivative(current_pos)  # Update rule
    new_y = y_function(new_x)
    current_pos = new_x
    print(current_pos)

    plt.plot(X, y)
    plt.scatter(current_pos, new_y, color="red")
    plt.pause(0.1)
    plt.clf()

# Final plot
plt.plot(X, y)
plt.scatter(current_pos, new_y, color="red")
plt.show()
