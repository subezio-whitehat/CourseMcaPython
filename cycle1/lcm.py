def comp_lcm(x,y):
    if x>y:
        grt=x
    else:
        grt=y

    while(True):
        if((grt%num1==0)and (grt%num2==0)):
            lcm=grt
            break
        grt=grt+1
    return lcm

num1=int(input("\nEnter the number1"))
num2=int(input("\nEnter the number2"))
print("\nThe LCM is",comp_lcm(num1,num2))

    
