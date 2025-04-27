from math import sqrt

def find_squares(a, b):
    s = []
    
    for i in range(a, b+1):
        if int(sqrt(i)) ** 2 == i:
            s.append(i)
    
    print(f"The squares between {a} and {b} are:", end=" ")
    
    if s:
        print(", ".join(map(str, s)))
    else:
        print("None")
        
def main():
    T = int(input("Enter the number of cases: "))
    
    if 0 <= T <= 100:
        for _ in range(T):
            A, B = map(int, input("Enter the range (A B): ").split())
            find_squares(A, B)   

if __name__ == "__main__":
    main()
