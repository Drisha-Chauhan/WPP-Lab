def next_permutation(s):
    s = list(s)
    n = len(s)

    i = n - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1

    if i == -1:
        return "no answer"

    j = n - 1
    while s[j] <= s[i]:
        j -= 1

    s[i], s[j] = s[j], s[i]
    s[i + 1:] = reversed(s[i + 1:])

    return "".join(s)

def main():
    t = int(input("Enter the number of test cases: ").strip())

    if not (1 <= t <= 100000):  
        print("Invalid number of test cases. Must be between 1 and 100000.")
        return

    results = []

    for _ in range(t):
        w = input("Enter the word: ").strip()

        if not (1 <= len(w) <= 100) or not w.islower():
            print("Invalid input. The word must contain only lowercase English letters and be at most 100 characters long.")
            return

        results.append(next_permutation(w))

    print("\nResults:")
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
