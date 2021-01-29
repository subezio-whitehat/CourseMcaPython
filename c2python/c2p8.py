#8. Get a string from an input string where all occurrences of first character replaced with
#‘$’, except first character.
#eg: onion -> oni$n
lis =[]
s=input("Enter String:")
for ch in s:
    if ch in lis:
        lis.append('$')
    else:
        lis.append (ch)
print(" ".join(str(i)for i in lis))