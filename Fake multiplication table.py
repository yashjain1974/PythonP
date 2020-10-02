

if __name__ == '__main__':
    list1 = []
    n=int(input("Enter Number\n"))
    for i in range(1, 11):
        a=n*i
        if(i==5):
            a=(n*i)+3


        list1.append(a)


    print(list1)
    for index,item in enumerate(list1):
        if(item%n!=0):
            print("It is Incorrect ")
        else:
            print(item)

