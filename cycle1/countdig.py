num=int(input("Enter the digit:"))
count=0
while(num>0):
    num=num//10
    count=count+1
print("\nThe no of digits in the number is:",count)
