class Pizze:
    def __init__(self, ibrahim):
        self.ibrahim = ibrahim

    @classmethod
    def veg(cls):
        return cls(["sdnf", "dhfj"])

    @classmethod
    def margeta(cls):
        return cls(["frty", "dfvb"])

    def __str__(self):
        return f"Pizze ingrdinxk is {self.ibrahim}"


Pizze1 = Pizze.veg()
Pizze2 = Pizze.margeta()
print(Pizze1)
print(Pizze2)


class Customer:
    def	__init__(self, name, balance=0):  
        self.name = name
        self.balance = balance
        print("The	init	method was called")
        
    def __str__(self):
        return 'Customer : ' +str(self.name)+ ' , balance: ' + str(self.balance) 
   
    def __add__(self, other): 
       return Customer("Test_Customer",self.balance + other)

cust = Customer("Lara de Silva") 
print(cust.balance) 
print(cust)
