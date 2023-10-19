class Shirt:
    fprice=1000
    def __init__(self,sid=0,sname=None,stype=None,price=0,size=None):
        self.sid=sid
        self.sname=sname
        self.stype=stype
        self.price=price 
        self.size=size 
    def Show(self):
        print("SHIRT ID        :",self.sid)
        print("SHIRT NAME      :",self.sname)
        print("SHIRT TYPE      :",self.stype)
        print("SHIRT PRICE     :",self.price)
        print("SHIRT SIZE      :",self.size)

    def Discount(self):
        if self.size=="small":
            fprice=1000
        elif self.size=="medium":    
            fprice= Shirt.fprice+Shirt.fprice*10/100
        elif self.size=="large":    
            fprice=Shirt.fprice+Shirt.fprice*20/100
        elif self.size=="extra large":    
            fprice= Shirt.fprice+Shirt.fprice*30/100     
        else:
            fprice=0
        return fprice    
    def __del__(self):
        print("OBJECT DESTROYED !!")  
s1=Shirt(101,"CHECKED","CASUAL",1000,"small")    
s1.Show()
a=s1.Discount()
print("FINAL PRICE FOR SHIRT IS :",a)
s2=Shirt(102,"FLORAL","CASUAL",1000,"medium")     
s2.Show()
a1=s2.Discount()
print("FINAL PRICE FOR SHIRT IS :",a1)
s3=Shirt(103,"POLKA DOT ","CASUAL",1000,"large")     
s3.Show()
a3=s3.Discount()
print("FINAL PRICE FOR SHIRT IS :",a3)
s4=Shirt(104,"DENIM ","CASUAL",1000,"extra large")     
s4.Show()
a4=s4.Discount()
print("FINAL PRICE FOR SHIRT IS :",a4)

