try:

 n=int(input("Enter the number of apple Harry Potter got:- "))
 min=int(input("Enter min number of people : "))
 max=int(input("Enter maximum number of people : "))

 list1=[]
 list2=[]
 for i in range(min,max+1):

    if n%i==0:
      list1.append(i)

    elif n%i!=0:
      list2.append(i)
except Exception as e:
    print(e)
    print("Strings are not allowed")
finally:
 print("Numbers which are divisible:",end=" ")
 print(list1)
 print("Numbers which are not divisible",end=" ")
 print(list2)


