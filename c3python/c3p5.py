
#5) Display the given pyramid with step number accepted from user. Eg: N=4 

def py(n):
  x=1
  for i in range(1, n+1):
    for j in range(1, i+1):
      print(x, end=" ")
      x=x+i
    x=i+1
    print("\r")
 
n=int(input("enter the limit : "))
py(n)