def compute_cross_product
import numpy as np
a = np.array([1, 2, 3])
b = np.array([1, 2, 5])
z = np.cross(a, b)

print(z)
import numpy as np

def compute_cross_product(a, b):
    z = np.cross(a, b)
    return z

# Example usage
a = np.array([1, 2, 3])
b = np.array([1, 2, 5])
result = compute_cross_product(a, b)

print(result)
