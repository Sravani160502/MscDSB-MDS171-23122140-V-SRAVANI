# Create a sportMart class, where you will have 
# -> inventory / shelf of items
# -> Orders of customers

# Create csv file which will store your inventory details and order details

# with the help of file handling technqiues in python, read the file and create an object for trinity store and populate the inventory items and orders into the trinity store.

# to make sure that you have added all the items in your file, use a display method to show your inventory and order history.

# class sportMart:
#     def __init__(self):
#         self.marts = {"invetory" : [] , "orders": [] }
        
#     def storeData(self,type,Itemname,price,quantity):
#         temp = {"name":Itemname, "Rate":price, "quantity":quantity}
#         self.marts[type].append(temp)

# create a menu driven program that will create new orders and update the inventory accordingly. export the final data to  the file

class sportMart:
    def __init__(self):
        self.inventory = {}
        self.orders = {}
    def createorder(self,OrderID,ItemName,Quantity,price,total):
        temp = {"orderid":OrderID, "ItemName":ItemName,"quantity":Quantity,"price":price,"total":total}

        self.orders[OrderID] = temp

    def createinventory(self,ProductID,ProductName,Quantity,Price):
        temp = {"productid":ProductID,"productname":ProductName,"quantity":Quantity,"price":Price}
        self.inventory[ProductID] = temp

    def printorders(self):
        print(self.orders)
    def printinventory(self):
        print(self.inventory)
trinity = sportMart()
orders = open("Orders.csv","r")
orders_headers = orders.readline()
orders_orders = orders.readlines()
for item in orders_orders:
    temp = item.strip().split(',')
    trinity.createorder(temp[0],temp[1],temp[2],temp[3],temp[4])

trinity.printorders()


    
Inventory = open("Inventory.csv","r")
Inventory_headers = Inventory.readline()
Inventory_Inventory = Inventory.readlines()
for item in Inventory_Inventory:
    temp = item.strip().split(',')
    trinity.createinventory(temp[0],temp[1],temp[2],temp[3])
trinity.printinventory()

def menu():
    print("1.Create Order")
    
    print("2. Update the inventory")
    print("3.printinventory")
    print("4.printorders")
    print("5.exit")
choice = int(input("enter your choice:"))
if choice == 1:
    OrderID = input("Enter Order ID:")
    ItemName = input("enter the ItemName:")
    quantity = int(input("enter the quantity:"))
    price = int(input("enter the price:"))
    total = int(input("enter the total:"))
                      
elif choice == 2:
    ProductID = input("Enter the ProductID:")
    ProductName = input("enter the ProductName:")
    quantity = int(input("enter the quantity:"))
    price = input("enter the price:")

elif choice == 3:
    trinity.printinventory("ProductID","ProductName","quantity","price")

elif choice == 4:
    trinity.printorders("OrderID","ItemName","quantity","price","total")

elif choice == 5:
    exit()
else: 
    print("Invalid Choice")
