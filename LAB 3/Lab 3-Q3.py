T= int(input())
Nums=[]

for i in range(1,T=1):
    
    N=int(input())
    Nums.append(N)
    
    if(T<0|T>25|N>10**10|N<0):
        exit(1)
        
    counts=[]
    
for i in range(1,T+1):
        
        x=Nums[i]
        
        while(x!=0):
            r=x%10
            count=0
            
            if(x%r==0):
                count=count+1
                
            counts.append(count)
            x/=10
            
for i in counts:
    print(i)            
    
                    

