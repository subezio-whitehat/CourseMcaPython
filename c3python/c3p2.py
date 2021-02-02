#Generate Fibonacci series of N terms

def fibonacci():
    limit = int(input("Enter the Number of terms:"))
    first = 0
    second = 1
    print(str(first))
    print("\n"+ str(second))
    for i in range(2,limit):
        next = first + second
        first = second
        second = next
        print("\n"+str(next))

fibonacci()