class Rectangle:
    def __init__ (self, len,bre) -> object:
        self.len = len
        self.bre = bre

    def area(self):
       return int(self.len * self.bre)
    def peri(self):
         return 2*(self.len+self.bre)
    def __del__(self):
        print('Object Deleted')
    def __lt__(self, other):
         if (self.area() < other.area()):
             print('2nd rectangle is larger')
         else:
             print('1st rectangle is larger')
    def display(self):
        print('Length of the rectangle is :', self.len)
        print('Breadth of the rectangle is :', self.bre)
l1=int(input('enter the length of rect1:'))
b1=int(input('enter the breadth of rect1:'))
rect=Rectangle(l1,b1)
a1=rect.area()
l2=int(input('enter the length of rect2:'))
b2=int(input('enter the breadth of rect2:'))
rect2=Rectangle(l2,b2)
a2=rect2.area()
print('Perimeter of the rectangle1 is:',rect.peri())
print('Area of the first rectangle is:',a1)
print('Perimeter of the 2nd rectangle is:',rect2.peri())
print('The area of second rectangle is:',a2)
print(rect<rect2)