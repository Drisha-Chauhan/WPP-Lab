def generate_fibonacci():  # Generate Fibonacci numbers up to 100
   
    fib_list = []
  
    a, b = 0, 1
  
    while a <= 100:  # Stop when Fibonacci number exceeds 100
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

def check(N, fib_list):  # Function to check if N is in the Fibonacci list
   
    if N in fib_list:
        print("IsFibo")
   
    else:
        print("IsNotFibo")

def main():
  
    T = int(input("No of test cases: "))
    
    fib_list = generate_fibonacci() 
    
    print(f"Enter {T} two digit numers ")
    
    for _ in range(T):
        N = int(input())
        check(N, fib_list)

main()
