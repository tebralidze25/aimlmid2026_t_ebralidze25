import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Manually extracted data points from the graph
x = np.array([-9.00, -7.00, -5.00, -3.00, -1.00, 1.00, 3.00, 5.00, 8.00, 9.30])
y = np.array([7.80, 6.60, 5.00, 2.70, 1.10, -0.70, -3.20, -4.60, -6.80, -8.10])

# Calculate Pearson correlation coefficient
r, p_value = pearsonr(x, y)

print("Pearson correlation coefficient:", r)
print("P-value:", p_value)

# Visualization
plt.figure()
plt.scatter(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot of Extracted Data Points")
plt.grid(True)
plt.show()
