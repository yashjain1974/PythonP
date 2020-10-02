import random
def player1(random_number):
 print("Welcome Player 1")
 print("Please choose number ")
 i=0
 k=0
 while(i<10):
  number=int(input("Enter Guessed number:-\n"))
  if(random_number>number):
      print("you Choose smaller number")
      print("Try again" )
      k+=1
  elif(random_number<number):
      print("You Choose greater number")
      print("Try again")
      k+=1
  else:
      print("You have Guessed right number")
      print(f"You have guessed right number in {k} times ")
      break


def player2(random_number):
    print("Welcome Player 2")
    print("Please choose number ")
    i = 0
    j = 0
    while (i < 10):
        number = int(input("Enter Guessed number:-\n"))
        if (random_number > number):
            print("you Choose smaller number")
            print("Try again")
            j += 1
        elif (random_number < number):
            print("You Choose greater number")
            print("Try again")
            j += 1
        else:
            print("You have Guessed right number")
            print(f"You have guessed right number in {j} time ")
            break

if __name__ == '__main__':
    a=int(input("Enter First Number:-"))
    b=int(input("Second number:-"))
    random_number=random.randint(a,b)
    print(random_number)
    player1(random_number)
    player2(random_number)


