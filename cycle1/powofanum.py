num=int(input("Enter the number:"))
p=int(input("\nEnter the required power:"))
i=0
if(p<0):
    print("\nThe power of given number is 1")
else:
    while(i<=p):
        num=num*p
        i=i+1
print("\nThe power of the number is:",num)
