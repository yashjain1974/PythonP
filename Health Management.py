def Health_Management():
    print("..................../Welcome to health management/........................")
    k=int(input("Enter 1 for take and 2 for retrieve\n"))
    a=int(input("Enter number from 1 ,2 or 3\n"
                "1 for Harry\n"
                "2 for Rohan\n"
                "3 for Hammid\n"))

    if k==1:
        if a==1:
            return harry()
        elif a==2:
            return rohan()
        elif a==3:
            return hammid()

    elif k == 2:
        if a == 1:
         return harry_read()
        elif a == 2:
         return rohan_read()
        elif a == 3:
         return hammid_read()

def getdate():
   import datetime
   return datetime.datetime.now()

z=getdate()

def harry():
    b = int(input("enter number from 1 or 2 \n"
                  "1 for Exercise\n"
                  "2 for Diet\n"))
    if(b==1):

        with open("harry exercise.txt","a") as f:
          f.write("\n\nEnter your exercise:\n")
          c=str(input("enter exercise\n"))
          f.write(str([str(z)]))
          f.write("\n")
          d=f.write(c)
          return(d)
    elif(b==2):
        with open("harry diet.txt","a") as y:
          y.write("\n\nEnter your diet:\n")
          e=str(input("Enter diet\n"))
          y.write(str([str(z)]))
          y.write("\n")
          g=y.write(e)
          return(g)

def rohan():
    b = int(input("enter number from 1 or 2 \n"
                  "1 for Exercise\n"
                  "2 for Diet\n"))
    if (b == 1):

        with open("rohan exercise.txt", "a") as f:
            f.write("\n\nEnter your exercise:\n")
            c=str(input("enter exercise\n"))
            f.write(str([str(z)]))
            f.write("\n")
            d = f.write(c)
            return (d)
    elif (b == 2):
        with open("rohan diet.txt", "a") as y:

            y.write("\n\nEnter your diet:\n")
            e = str(input("enter diet\n"))
            y.write(str([str(z)]))
            y.write("\n")
            g = y.write(e)
            return (g)

def hammid():
    b = int(input("enter number from 1 or 2 \n"
                  "1 for Exercise\n"
                  "2 for Diet\n"))
    if (b == 1):

        with open("hammid exercise.txt", "a") as f:
            f.write("\n\nEnter your exercise:\n")
            c = str(input("enter exercise\n"))
            f.write(str([str(z)]))
            f.write("\n")
            d = f.write(c)
            return (d)
    elif (b == 2):
        with open("hammid diet.txt", "a") as y:
            y.write("\n\nEnter your diet:\n")
            e = str(input("enter diet\n"))
            y.write(str([str(z)]))
            y.write("\n")
            g = y.write(e)
            return (g)

'''def again():
     while(True):
      cal_again=input("do you want to run again? Please type y or n")
      if cal_again=="y":
       return(Health_Management())
       continue
      elif cal_again=="n":
       return("see you later")
       break'''

def harry_read():
    b = int(input("enter number from 1 or 2 \n"
                  "1 for Exercise\n"
                  "2 for Diet\n"))
    if (b == 1):

        with open("harry exercise.txt", "r") as f:
            d = f.read()
            print (d)
    elif (b == 2):
        with open("harry diet.txt", "r") as y:
            g = y.read()
            print (g)
def rohan_read():
    b = int(input("enter number from 1 or 2 \n"
                  "1 for Exercise\n"
                  "2 for Diet\n"))
    if (b == 1):

        with open("rohan exercise.txt", "r") as f:
            d = f.read()
            print (d)
    elif (b == 2):
        with open("rohan diet.txt", "r") as y:
            g = y.read()
            print (g)
def hammid_read():
    b = int(input("enter number from 1 or 2 \n"
                  "1 for Exercise\n"
                  "2 for Diet\n"))
    if (b == 1):

        with open("hammid exercise.txt", "r") as f:
            d = f.read()
            print (d)
    elif (b == 2):
        with open("hammid diet.txt", "r") as y:
            g = y.read()
            print(g)
Health_Management()
while(True):
    cal_again = input("do you want to run again? Please type y for yes or n for no\n")
    if cal_again=="y":
        Health_Management()
        continue
    elif cal_again=="n":
        print("see you later")
        break
