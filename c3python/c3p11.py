#11) Write lambda functions to find area of square, rectangle and triangle.

a=int(input("enter the side of square : "))
sq_area=lambda a:a**2
print("area of the square is : ",sq_area(a))
l=int(input("enter length : "))
w=int(input("enter width : "))
rect_area=lambda l,w : l*w
print("area of the rectangle is : ",rect_area(l,w))
a=int(input("enter the value of first side : "))
b=int(input("enter the value of second side : "))
c=int(input("enter the value of third side : "))
s=(a+b+c)/2
t_area=lambda s,a,b,c : (s*(s-a)*(s-b)*(s-c))**0.5
print("area of triangle :",t_area(s,a,b,c))