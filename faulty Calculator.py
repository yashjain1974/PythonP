
def calculator():
  a=int(input("enter a number "))
  b=int(input("enter a number "))
  c=input("enter operator ")
  sum=a+b
  divide=a/b
  subtract=a-b
  multiply=a*b
  if(a==45 and b==3 and c=="*"):
    print(555)
  elif(a==56 and b==9 and c=="+"):
    print(77)
  elif(a==56 and b==6 and c=="/"):
    print(4)
  elif c=="+":
    print("sum is=",sum)
  elif c=="-":
    print("subtract is=",subtract)
  elif c=="/":
    print("divide is",divide)
  elif c=="*":
    print("multiply is",multiply)
  else:
    print("not defined")
calculator()
while True:
    a=input("Do you want to calculate again :"
            "y for yes "
            "n for no")
    if(a=="y"):
        calculator()
    elif(a=="n"):
        "See you later"
        break

