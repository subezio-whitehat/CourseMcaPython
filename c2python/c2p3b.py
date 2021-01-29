#((b) Square of N numbers
num=int(input("Enter the number:"))
lis1=[]
lim=num+1
for i in range(lim):
    temp=i*i
    lis1.append(temp)
i=i+1
print(lis1)