L = int(input("Enter L: "))
R = int(input("Enter R: "))

max_xor = 0  

for i in range(L, R + 1):
    for j in range(i, R + 1):  
        max_xor = max(max_xor, i ^ j)  

print(max_xor)
