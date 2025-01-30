import random

random_list=[random.randint(0,1)for _ in range(1,100)]

print(random_list)

current_zeroes=0
max_zeroes=0

for number in random_list:
    if number==0:
        current_zeroes+=1
    else:
        current_zeroes=0
        
    if current_zeroes>max_zeroes:
        max_zeroes=current_zeroes
        
print(max_zeroes)
