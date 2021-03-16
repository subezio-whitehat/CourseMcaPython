# Python program to copy odd lines of one file to other
l=[]
f=open("D:\hello.txt",'r')
for i in f:
    l.append(i)
count=len(l)
f2=open("demo1.txt","x")
for i in range(0,count,2):
    f2.write(l[i])
f2.close()
