#5. Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.
lst = []  
n = int(input("Enter size of list or number of elements thet you wants to enter : ")) 
for i in range(0, n): 
    elem= int(input())
    if(elem>=100):
        lst.append('over')
    else:
        lst.append(elem) 
print(lst) 