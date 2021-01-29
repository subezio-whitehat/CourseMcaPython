#20) From a list of integers, create a list removing even numbers.
list = [11, 22, 33, 44, 55]
print("\nOriginal list:")
print(list)
for i  in list:
	if(i%2 == 0):
	    list.remove(i)
print("\nlist after removing EVEN numbers:")
print(list)