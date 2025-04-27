def decode_message(s, index=0, path="", res=[]):
    if index == len(s):
        res.append(path)
        return
    for i in range(1, 3):
        if index + i <= len(s):
            num = int(s[index:index + i])
            if 1 <= num <= 26:
                decode_message(s, index + i, path + chr(num + 64), res)
    return res

encoded = input("Enter encoded message: ")
print("Decoded messages:", decode_message(encoded))
