#1.Program to read a file line by line and add it to a list
l=[]
f=open("D:\hello.txt",'r')
for i in f:
    l.append(i)

print(l)