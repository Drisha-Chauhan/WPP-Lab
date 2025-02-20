def check_pangram(s):
    s = s.lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    
    if set(s) >= alphabet:
        print("Pangram")
    else:
        print("Not Pangram")

def main():
    s = input("Enter a sentence: ")
    check_pangram(s)

if __name__ == "__main__":
    main()
