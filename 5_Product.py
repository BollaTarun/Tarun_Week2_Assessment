
class Product:

    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    
    def check_availability(self,quantity):
        if quantity<=self.stock:
            print("Required Product Quantity is Available!!.")
        else:
            print("Required Product Quantity is not Available!!.")

    def product_details(self):
        print(f"Product Details :\nName\t: {self.name}\nPrice\t: {self.price}\nQuantity : {self.stock}")


p=Product("Pen",10.00,30)
p.check_availability(20)
p.product_details()


p=Product(input("Enter the Name of the Product :\n"),int(input("Enter the Price of the Product :\n")),int(input("Enter the Quantity of the Product :\n")))
p.check_availability(int(input("Enter the Quantity of Product you want to check:\n")))
p.product_details()