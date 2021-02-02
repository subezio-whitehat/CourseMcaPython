#3 Find the sum of all items in a list

ls = []
sum = 0
limit = int(input("Enter the limit of List:"))
for i in range(limit):
    num = int(input("Enter the element:"))
    ls.append(num)
    sum = sum + ls[i]
print(sum)    