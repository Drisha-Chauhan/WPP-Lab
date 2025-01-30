s = input("Enter the main string: ")
sub = input("Enter the substring to find: ")

s_len = len(s)
sub_len = len(sub)

index = -1

for i in range(s_len - sub_len, -1, -1):
    match = True
    for j in range(sub_len):
        if s[i + j] != sub[j]:
            match = False
            break
    if match:
        index = i
        break

print(index)