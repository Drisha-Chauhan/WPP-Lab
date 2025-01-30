text = input("Enter the original text: ")
old = input("Enter the substring to replace: ")
new = input("Enter the new substring: ")

result = ""
i = 0
old_len = len(old)
count = 0

while i < len(text):
    if text[i:i + old_len] == old:
        result += new
        i += old_len
        count += 1
    else:
        result += text[i]
        i += 1

print(result)
print("Occurrences replaced:", count)
