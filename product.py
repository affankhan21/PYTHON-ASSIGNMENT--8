class Product:
    dicount=0
    def __init__(self,pid=1,pname="PEN",price=20,quantity=3):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
    def Show(self):
        print("PRODUCT ID       :",self.pid)    
        print("PRODUCT NAME     :",self.pname)
        print("PRODUCT PRICE    :",self.price)
        print("PRODUCT QUANTITY :",self.quantity)
    def Discount(self):
        if self.price>50:
            dicount=self.price-self.price*10/100
        else:
             dicount=self.price-self.price*5/100
        return dicount       

    def __del__(self):
        print("OBJECT DESTROYED !!")
p1=Product()
p1.Show()
a=p1.Discount()
print("FINAL PRICE IS :",a)
p2=Product(101,"BOOK",60,2)
p2.Show()
a2=p2.Discount()
print("FINAL PRICE IS :",a2)

