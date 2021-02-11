#8) Accept a list of words and return length of longest word. 

l=[]
n= int(input("enter the number of elements in list : "))
for i in range(1,n+1):
    x=input()
    l.append(x)
max=len(l[0])
temp=l[0]
for j in l:
    if(len(j)>max):
       max=len(j)
       temp=j
print("the word with the longest length is :",temp)