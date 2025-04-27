def cuts(k):    
    rows = k // 2
    columns = k - rows  
    pieces = rows * columns
    print(pieces)

def main():
    t = int(input("Enter number of test cases: "))  
    nums = list(map(int, input("Enter values: ").split()))  

    for i in range(t):
        cuts(nums[i])  

if __name__ == "__main__":
    main()
