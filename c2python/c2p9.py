#9. Create a string from given string where first and last characters exchanged. [eg: python -
#> nythop]
s=input("\nEnter a string:")
newstr=s[-1] + s[1:-1] + s[0]
print(newstr)