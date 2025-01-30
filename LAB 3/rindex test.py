parent=input("Enter the parent string: ")
sub_string=input("Enter the sub string: ")

x=1
for i in range(len(parent)-len(sub_string),-1,-1): #reducing the maximum i value ensures 
      s_1= parent[i:i+len(sub_string)] #s_1 does not go out of bound; it is applicable in cases where no matching sub string is found 
      if s_1==sub_string:
                x=i
                
                break
                
print(f"rindex={x}")               
