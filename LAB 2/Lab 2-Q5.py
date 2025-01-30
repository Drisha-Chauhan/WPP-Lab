names = []
for _ in range(10):
    name = input("Enter the student's name: ")[:15]
    names.append(name[::-1])

for name in names:
    print(name)
