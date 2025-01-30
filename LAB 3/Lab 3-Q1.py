word= list(input("Enter a word: ")) #converted to list as strings are immutable

for i in range (1,len(word),2):
    word[i]= word[i].upper() #Every even position character is capitalised

new_word= ''.join(word) #converted the list back to a string 
print(new_word)
    
    