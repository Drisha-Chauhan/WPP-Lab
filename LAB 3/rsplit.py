s = input("Enter the string: ")
sep = input("Enter the separator: ")

parts = []
temp = []

i = len(s) - 1

while i >= 0:
    temp.insert(0, s[i])  
    if len(temp) >= len(sep) and ''.join(temp[:len(sep)]) == sep:
        parts.insert(0, ''.join(temp[len(sep):]))  
        temp = [] 
    i -= 1

if temp:
    parts.insert(0, ''.join(temp)) 

print(parts)
