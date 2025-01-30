Names={}
flag=1

while(flag==1):
    
    Name = input("Enter the name of the product(enter 1 to exit): ")
    
    Price= int(input("Price: "))
    
    if((Name)=="1"):
        flag=0
    Names[Name]= Price 
    
 

while(flag==5):
    
    enquire= input("Product to be inquired(enter 1 to exit): ")
    
    print("Price: ", Names[enquire])
    
    if(int(enquire)==1):
        
        print("Thank you")
        flag=0
        
    if enquire in Names:
        continue
    else:
        print("Product does not exist")
        exit(1)    
        
        
    