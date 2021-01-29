#15 Print out all colors from color-list1 not contained in color-list2.
color_list_1 =set()
color_list_2 = set()
limit1=int(input("Enter l1 limit:"))
limit2=int(input("Enter l2 limit:"))
for i in range(0,limit1):
   color1=input("Enter color to l1:")
   color_list_1.add(color1)
for j in range(0,limit2):
   color2=input("Enter color to l2:")
   color_list_2.add(color2)
print(color_list_1.difference(color_list_2))