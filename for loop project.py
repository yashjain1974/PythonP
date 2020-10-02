a=int(input("enter a number"))
b=int(input("enter 0 0r 1"))
i=0
while(a>i):
    i += 1
    if b==1:
        print("*"*i)
    elif b==0:
        print("*"*(a-i+1))
