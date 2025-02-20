def make_palindromes(word):
    count = 0
    s = list(word)
    
    for i in range(0, len(word) // 2):
       
        count += abs(ord(s[len(word) - i - 1]) - ord(s[i]))
    
        if s[len(word) - i - 1] > s[i]:
            s[len(word) - i - 1] = s[i]
        else:
            s[i] = s[len(word) - i - 1]
    
    return count

def main():
    T = int(input("Enter the no of cases: "))
    
    if 0 <= T <= 10:
        for _ in range(T):
            string = input("Enter the string: ")
            print(make_palindromes(string))
    
    return 0

if __name__ == "__main__":
    main()
