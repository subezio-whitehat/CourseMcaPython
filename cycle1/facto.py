x=int(input("Enter the number:"))
fact=1
i=0
for i in range(1,x+1):
    fact=fact*i
print("\nThe factorial of {0} is:".format(x),fact)
