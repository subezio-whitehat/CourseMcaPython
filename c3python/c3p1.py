#Factorial of a Number
def factorial():
    num = int(input("Enter Number:"))
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    print("Factorial of "+ str(num)+": "+str(fact))

factorial()