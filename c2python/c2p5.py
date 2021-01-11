lst=[]
subs="a"
n=int(input("\nEnter the number of frst names:"))
for n in range(0,n):
    fname=input("\nEnter the name:")
    lst.append(fname)
count=lst.count(subs)
print("\nThe list is:",lst)
print("\nThe count of a in list is:",count)