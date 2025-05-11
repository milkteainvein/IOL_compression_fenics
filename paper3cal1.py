import numpy as np
import matplotlib.pyplot as plt
# Example: Load data from a CSV or array
# Replace this with your actual data loading method
# For example, if your data is in a CSV file:
# data = np.loadtxt('your_data.csv', delimiter=',')

# Or define data manually for testing
# Example data format: [ [x1, y1], [x2, y2], ... ]

X_COORDS = 19.56

with open("3.csv", encoding="utf-8-sig") as f:
    data = np.loadtxt(f, delimiter=",")



# Split into x and y
x = data[:, 0]
y = data[:, 1]

# Fit linear model: y = mx + b
coeffs = np.polyfit(x, y, deg=1)  # coeffs[0] = m, coeffs[1] = b

# Generate fitted line
y_fit = coeffs[0] * x + coeffs[1]

# Print the function
print(f"Fitted linear function: y = {coeffs[0]:.4f}x + {coeffs[1]:.4f}")
# Predict y for a new x value
x_new = X_COORDS
y_new = coeffs[0] * x_new + coeffs[1]
print(f"Predicted y for x = {x_new}: {y_new:.4f}")

# Plot
plt.scatter(x, y, label='Data Points')
plt.plot(x, y_fit, color='red', label='Fitted Line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Linear Fit')
plt.show()