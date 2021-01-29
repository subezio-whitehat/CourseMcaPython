#14. Accept an integer n and compute n+nn+nnn.
num=int(input("\nEnter the number:"))
val=num+num*num+num*num*num
print("\nSum is:%d" %(val))