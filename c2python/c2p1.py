final=int(input("Enter the year"))
current=int(input("\nEnter the current year"))
x=current
while(x<=final):
    if(x%4)==0:
        print("\nleap year=:",x)
    x=x+1
