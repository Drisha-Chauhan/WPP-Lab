import numpy as np

def generate_odd_magic_square(n):
    magic_square = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        magic_square[i, j] = num
        i, j = (i - 1) % n, (j + 1) % n
        if magic_square[i, j]:
            i = (i + 2) % n
            j = (j - 1) % n
    return magic_square

def generate_even_magic_square(n):
    magic_square = np.arange(1, n * n + 1).reshape(n, n)
    swap_indices = [(i, j) for i in range(n) for j in range(n) if (i % 4 == j % 4) or (i % 4 + j % 4 == 3)]
    for i, j in swap_indices:
        magic_square[i, j] = n * n + 1 - magic_square[i, j]
    return magic_square

for N in [4, 5, 6, 7, 8]:
    print(f"\nMagic Square for N={N}\n", generate_odd_magic_square(N) if N % 2 else generate_even_magic_square(N))
