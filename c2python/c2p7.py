#7. Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums
#to same value (c) whether any value occur in both
list1=[]
list2=[]
sum1=0
sum2=0
n=int(input("\nEnter the number of elements in 1st list:"))
for i in range(0,n):
    fnum=input("\nEnter the number:")
    list1.append(fnum)
n2=int(input("\nEnter the number of elements in 2nd list:"))
for j in range(0,n2):
    fnum2=input("\nEnter the number:")
    list2.append(fnum2)
if(len(list1)==len(list2)):
    print("\nBoth lists are of length:",len(list1))
else:
    print("\nThe lists are not of same length!!")
for k in range(0,n):
   sum1=sum1+int(list1[k])
for l in range(0,n2):
   sum2=sum2+int(list2[l])
if sum1==sum2:
    print("\nLists are of same sum!!")
else:
    print("\nlists are not of same sum!!")
for i in range(0,n):
    for j in range(0,n2):
        if(list1[i]==list2[j]):
            print("\n%s is present in both lists!"%list1[i])
            exit()
print("\nNo repetition in lists!")
