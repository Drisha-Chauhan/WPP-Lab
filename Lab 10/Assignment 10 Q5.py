import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 4*x - 2

def bisection_method(a, b, tol=1e-6):
    updates = []
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        updates.append(c)
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return np.array(updates)

a, b = -3, 3
roots = bisection_method(a, b)

x_vals = np.linspace(a, b, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x)")
plt.axhline(0, color='black', linewidth=0.5)
plt.scatter(roots, [f(r) for r in roots], color='red', label="Bisection Steps")
plt.legend()
plt.show()
