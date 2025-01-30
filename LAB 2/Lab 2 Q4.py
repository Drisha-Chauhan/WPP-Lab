numbers = range(1, 10001)
equivalence_classes = {i: [] for i in range(5)}

for num in numbers:
    equivalence_classes[num % 5].append(num)

union_of_classes = set().union(*equivalence_classes.values())
is_valid = set(numbers) == union_of_classes

print("Equivalence Classes:", equivalence_classes)
print("Is Valid:", is_valid)
