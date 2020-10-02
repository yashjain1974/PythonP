print("                       First program                       ")
n=0
i=0
try:

    while(n<=10):

        i=int(input("Enter a number \n"))
        print("(", 10 - n, "number of guesses left )")
        n += 1
        if(i==18):
          print("You guessed right number")
          print(n,"number of guesses to finish")
          i+=1
          break

        elif(i>18):
          print("Greater than number")
        else:
          print("Smaller than number")


    if(n>10):
      print("game over your secret number is 18")
except Exception as e:
    print(e)



                          # third method.............
print("                       Second program                           ")
for i in range(1, 5):
    a = int(input("enter a number\n"))
    print("number of attempt left", 5 - i)
    if (a == 90):
        print("you won")
        break
    elif (a > 90):
        print("you entered greater number")
    else:
        print("you entered smaller number")
if (i > 10):
        print("game over")
