#2.Display future leap years from current year to a final year entered by user.
final=int(input("Enter the year"))
current=int(input("\nEnter the current year"))
x=current
while(x<=final):
    if((x%4==0) and (x%100!=0)) or (x%400==0):
        print("\nleap year=:",x)
    x=x+1
