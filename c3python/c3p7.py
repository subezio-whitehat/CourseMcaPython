#7) Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’.

s=input("enter any string : ")
if s.endswith("ing") :
  s+="ly"
else :
  s+="ing"
print("modified string : ",s)