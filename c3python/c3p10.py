#10) Generate all factors of a number. 

n=int(input("enter any number : "))
i=1
print("all factors of",n,"are :")
while i<=n:
  if n%i==0:
    print(i)
  i=i+1