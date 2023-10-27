class MSCDSB:

    def __init__(self): # Member function
        # Data members / Properties / Attribute
        self.name = "MSC DS B"
        self.students = ["A","B","C"]
    
    def printstudents(self):
        for student in self.students:
            print(student)



obj = MSCDSB()
print(obj.name)
print(obj.students)
obj.printstudents()



class car:

    def __init__(self,mfg,mdl,yer):
        self.Manufacturer = mfg
        self.model = mdl 
        self.Year = yer

bmw = car("BMW","F series",2020)
print(bmw.Manufacturer)

ferari = car ("Ferrari","A series",2023)
print(ferari.model)










class food:

    def __init__ (self,dish,rating,amt):
        self.dish = dish
        self.rating = rating
        self.amount = amt

def __str__(self):
    return self.Manufacturer
    

# create a class resturant,that accepts 
# itemme and qty as input 
# inside your class you are having the item 
# and its cost(unit price)as a dictionary
# create a functin calculate totalcost
#that prints the itemname, qty& totalcost

class restaurant:
    def __init__(self,itemname,qty):
        self.itemname=itemname
        self.qty=qty
        self.menuItems={"rice":30,"chickhen":100,"dal":40,"gulabjamun":100}
    def totalcost(self):
        print("total cost of the order")
        print("Item\t:",self.itemname)
        print("Quantity\t:",self.qty)
        total = self.qty * self.menuItems[self.itemname]
        print("Total\t:",total)

order = restaurant("rice",4)
order.totalcost()
order = restaurant("chickhen",8)
order.totalcost()





#define a class expense tracker that stores the 
#expenses and income in a dictionary
#implement the method to
# -store the transaction:
#-view transaction;
# -calculate the total expense/income



class expenseTracker:
    def __init__(self):
        self.expenseDict = {"income":[],"expense":[],}
        pass
    def store_transactions(self,type,amt,category,date,details):
        trans = {"Amount":amt,"Category":category,"Date":date,"Details":details}
        if type == "income":
            self.expenseDict['income'].append(trans)
        else:
            self.expenseDict['expense'].append(trans)  

def view_transaction(self):
    print("Your Income:")
    for item in self.expenseDict['income']:
        print(item)
    print("Your Expenses:")
    for item in self.expenseDict['expense']:
        print(item)

def calculate_transactions(self):
    total_income = 0
    for item in self.expenseDict['income']:
        total_income += item["Amount"]
    print("Total Expenses\t:\t", total_income)

    total_expense = 0
    for item in self.expenseDict['expense']:
        total_expense += item["Amount"]
    print("Total Expenses\t:\t", total_expense)

#define a menu that will let users to enter  expense,view expenses
#or income,get totals in each and exit from the program

# define a class expense tracker that stores the
# expenses and income in a dictionary
# implement the method to
# - store the transaction;
# - view transactions;
# - calculate the total expense/income


class expenseTracker:
    def __init__(self):
        self.expenseDict = {
            "income": [],
            "expense": [],
        }

    def store_transactions(self, type, amt, category, date, details):
        trans = {
            "Amount": amt,
            "Category": category,
            "Date": date,
            "Details": details,
        }
        if type == "income":
            self.expenseDict['income'].append(trans)
        else:
            self.expenseDict['expense'].append(trans)

    def view_transactions(self):
        print("Your Income:")
        for item in self.expenseDict['income']:
            print(item)
        print("Your Expenses:")
        for item in self.expenseDict['expense']:
            print(item)

    def calculate_transactions(self):
        total_income = 0
        for item in self.expenseDict['income']:
            total_income += item["Amount"]
        print("Total Income\t:\t", total_income)

        total_expense = 0
        for item in self.expenseDict['expense']:
            total_expense += item["Amount"]
        print("Total Expenses\t:\t", total_expense)

# define a menu that will let users to enter expense, view expenses
# or income, get totals in each and exit from the program


def collectInput():
    amt = int(input("Enter the amout: "))
    category = input("Enter Category: ")
    date = input("Enter Date (DD/MM/YYYY): ")
    details = input("Enter description: ")
    return amt, category, date, details


myexpense = expenseTracker()

while True:
    print("...MY EXPENSE TRACKER...")
    print("1. Record Income")
    print("2. Record Expense")
    print("3. View Records")
    print("4. View My Spendings")
    print("5. Exit")

    choice = int(input("Enter your choice: ").strip())  

    if choice == 1:
        print("Enter the details of income")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("income", amt, category, date, details)
    elif choice == 2:
        print("Enter the details of expense")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("expense", amt, category, date, details)
    elif choice == 3:
        myexpense.view_transactions()
    elif choice == 4:
        myexpense.calculate_transactions()
    elif choice == 5:
        exit()
    else:
        print("In valid choice")


#create a method in the class
#to export the details in the form of csv
#add export details to a file in the menu options

