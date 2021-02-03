
def charcount():
    st=input("\nEnter the string:")
    count=0
    for i in range(0,len(st)):
        count=count+1
    print("\nThe no of char is:%s"% (count))
charcount()