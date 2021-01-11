word=input("Enter the word:")
ordinal=[]
i=0
while(i<len(word)):
     temp=ord(word[i])
     ordinal.append(temp)
     i=i+1
print(ordinal)