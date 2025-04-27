import numpy as np

arr = np.array(["apple", "banana", "cherry", "date"])
left_justified = np.array([s.ljust(15, '_') for s in arr])
right_justified = np.array([s.rjust(15, '_') for s in arr])
centered = np.array([s.center(15, '_') for s in arr])

print("\nLeft Justified:\n", left_justified)
print("\nRight Justified:\n", right_justified)
print("\nCentered:\n", centered)
