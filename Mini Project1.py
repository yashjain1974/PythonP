'''
Create a library class
display book
lend book
add book
return book
'''
'''
def library():
 class Library:
    def __init__(self,Sr_no,bookname,bookcost):
        self.Srno=Sr_no
        self.Bookname=bookname
        self.Bookcost=bookcost
    def Book_details(self):
        return f"\nBook Sr_no: {self.Srno}" \
            f"\nBook Name: {self.Bookname}" \
            f"\nBook Cost: {self.Bookcost}"
 a=int(input("Enter Serial no\n"))
 b=str(input("Enter Book Name\n"))
 c=str(input("Enter Book cost\n"))
 b=Library(a,b,c)
 Book=b.Book_details()
 print(Book)
library()
def Display():'''

# while (True):
#  a=str(input("Enter Yes or no"))
#  if a=="yes":
#      library()
#      continue
#  else:
#      print("See you later")
#      break

class Library:
    def __init__(self,Sr_no,bookname,bookcost):

        self.Bookname = []
        self.Srno = []
        self.Bookcost = []
        self.Dict={}
    def displaybooks(self):
        print("This Is Available Books In our Store" )
        print(self.Bookname,end=" ")
        print(self.Srno,end=" ")
        print(self.Bookcost)

    def lendbook(self,user,book):
        if book not in self.Dict.keys():
            self.Dict.update({book:user})
            print (f"You Succesfully Lended Book {self.Bookname} in Library")
        else:
            print(f"Book is already in The Library as {self.Dict[book]}")
    def add(self,Srno,book,cost):
        self.Srno.append(Srno)
        self.Bookname.append(book)
        self.Bookcost.append(cost)
        print(f"{book} has been succesfully added in book list")
    def return_book(self,book):
        self.Bookname.remove(book)
if __name__ == '__main__':
    harry=Library(1,["harry potter"],20)
    while(True):
        print ("Welcome to the Library. Enter Your Choice To Continue")
        print("1.Display\n"
              "2.Add\n"
              "3.Lend\n"
              "4.Return")
        a=int(input("Choose Number"))
        if a==1:
            harry.displaybooks()
        elif a==2:
            b=str(input(("Enter Book name to add ")))
            c=str(input(("Enter Book Serial no to add ")))
            d =str(input(("Enter Book Cost to add ")))
            harry.add(b,c,d)
        elif a==3:
            c = str(input(("Enter Book name to Lend ")))
            e=str(input(("Enter User name to lend ")))
            harry.lendbook(e,c)
        elif a==4:
            d = str(input(("Enter Book name to remove ")))
            harry.return_book(d)
        else:
            print ("Not a valid Option")

















