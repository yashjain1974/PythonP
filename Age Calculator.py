print("/-------------------Age/DOB Calculator------------------/")
a=int(input("Enter 1 or 2\n"
              "1 By Age\n"
              "2 By Date of birth\n"))
current_year=int(input("enter current year"))
if a==1:
    age=int(input("Enter your age "))
    b=int(input("Enter year to know your age in Respective year "))
    d=(b-current_year)+age
    if d<0:
        print("You are not born yet")
    else:
     print("your age in Respective year is",d)
     print("Your DOB is",current_year-age)
     print("you will turn 100 on :", current_year+(100-age))
elif a==2:
    DOB=int(input("Enter your Birth year "))
    b = int(input("Enter year to know your age in Respective year "))
    d=b-DOB
    if d<0:
        print("You are not born yet")
    else:
     print("your Present age is", current_year-DOB)
     print("your age in given year is",d)
     print("you will turn 100 on :",DOB+100)