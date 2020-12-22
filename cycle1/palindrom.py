num=int(input("Enter the number:"))
rev=0
temp=num
while(num>0):
    rem=num%10
    rev=(rev*10)+rem
    num=num//10

if(rev==temp):
    print("\nThe number is a palindrome")
else:
    print("\nThe number is not a palindrome")
