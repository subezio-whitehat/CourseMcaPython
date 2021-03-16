class time :
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __add__(self, other):
        return self.hour+other.hour,self.minute+other.minute,self.second+other.second
print('***TIME 1***')
h=int(input('Enter the fist time hour:'))
m=int(input('Enter the first time minute:'))
s=int(input('Ente the first time second:'))
t1=time(h,m,s)
print('***TIME 2***')
h2=int(input('Enter the second time hour:'))
m2=int(input('Enter the second time minute:'))
s2=int(input('Ente the second time second:'))
t2=time(h2,m2,s2)
print('The new time !!!')
t3 = t1 + t2
print('The updated time is:',t3)