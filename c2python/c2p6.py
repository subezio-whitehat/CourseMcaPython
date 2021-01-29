#6. Store a list of first names. Count the occurrences of ‘a’ within the list
lst=[]
subs="a"
count=0
n=int(input("\nEnter the number of frst names:"))
for n in range(0,n):
    fname=input("\nEnter the name:")
    lst.append(fname)
for x in lst:
    if subs in x:
        count=count+1
        
print("\nThe list is:",lst)
print("\nThe count of a in list is:",count)