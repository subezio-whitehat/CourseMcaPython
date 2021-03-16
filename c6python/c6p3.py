f=open("D:\csv.csv","r")
f_contents=f.readlines()
list1=list(f_contents)
print(list1)
f.close()

#method 2

import csv
with open('D:\csv.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar='|')
 for row in data:
   print(', '.join(row))