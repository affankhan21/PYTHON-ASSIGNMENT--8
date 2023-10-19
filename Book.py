class Book:
    bCount=0
    def __init__(self,bid=101,bname="THE LINUX INTERFACE",author=" MICHAEL KERISK",price=5053):
        self.bid=bid
        self.bname=bname
        self.author=author
        self.price=price
        Book.bCount+=1
    def Showbook(self):
        print("BOOK ID     :",self.bid)
        print("BOOK NAME   :",self.bname)
        print("BOOK AUTHOR :",self.author)
        print("BOOK PRICE  :",self.price)
    def CountoOjects():
        print("NUMBER OF OBJECTS CREATED ARE =",Book.bCount)    
    def __del__(self):
        print("OBJECT IS DESTROYED!!") 
Book.CountoOjects()       
B1=Book()
B1.Showbook()
Book.CountoOjects()
b2=Book(102,"LET US C","YASHWANT KANETKAR",335)
b2.Showbook()
Book.CountoOjects()


   