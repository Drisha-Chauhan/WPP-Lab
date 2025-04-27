import numpy as np

N = int(input("Enter the number of points (N >= 10): "))
points = np.random.rand(N, 2) * 100
r = np.sqrt(points[:, 0]**2 + points[:, 1]**2)
theta = np.arctan2(points[:, 1], points[:, 0])
polar_points = np.column_stack((r, theta))

print("\nCartesian Points:\n", points)
print("\nPolar Coordinates:\n", polar_points)

