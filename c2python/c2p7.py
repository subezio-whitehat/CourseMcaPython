lis = []
s=input("Enter String:")
for ch in s:
    if ch in lis:
        lis.append('$')
    else:
        lis.append (ch)
print(" ".join(str(i)for i in lis))