def even_case(N):  
   
    height = 1  
    
    for i in range(N // 2):  
        height *= 2
        height += 1
    return height

def cycle_height(N):  
  
    if N % 2 == 0:
        return even_case(N)  
  
    else:
        return even_case(N - 1) + 1  

def main():
   
    T = int(input("Enter number of cases: "))  
    
    results = []  

    for i in range(T):  
        N = int(input())
        results.append(cycle_height(N))

    for res in results:  
        print(res)

main()
