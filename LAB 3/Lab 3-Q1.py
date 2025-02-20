def digital_root(N):  # Function for finding digital root
    
    digit_sum = 0

    while N > 0:  # Loop for finding sum of digits
        r = N % 10
        digit_sum += r
        N //= 10 

    if digit_sum > 9:  # Recursion if sum is not a single digit
        
        return digital_root(digit_sum)
 
    else:
        return digit_sum  # Return the single-digit sum

def main():
    N = int(input("Enter any number: "))
   
    s = digital_root(N)
   
    print(f"Digital Root of {N} is {s}")

main()
