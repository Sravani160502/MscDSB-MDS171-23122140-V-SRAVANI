
class stk:

    def __init__(self):
        self.stack = []

#Push function is used to add values to the stack
    def push(self,item):
        self.stack.append(item)
        print(self.stack)
        
    
#Pop function remove the uppermost item
    def pop(self,item):
        self.stack.pop(item)
        print(self.stack)

#Tofind length of stack
    def length(self):
        print(len(self.stack))

#To print the items in stack
    def item(self):
        print(self.stack)
        print(self.stack[len(self.stack)-1])



#To check if stack is empty
    def empty(self):
        if len(self.stack) == 0:
            print("The stack is empty")
        else:
            print("The stack is not empty") 


stack_1 =  stk()
# stack_1.push('pen')
# stack_1.push('pencil')
# stack_1.push('laptop')
# stack_1.pop(2)
# stack_1.empty()
# stack_1.item()

while True:
    choice = int(input("Enter your choice").strip())
    
    if choice ==1:
        stack_1.push(input("Enter the items to be added in the stack"))
    elif choice ==2:
        stack_1.pop(int(input("Enter the index of item you want to remove")))
    elif choice ==3:
        stack_1.length()
    elif choice ==4:
        stack_1.item()
    elif choice ==5:
        stack_1.empty()
    elif choice == 6:
        exit()
    else:
        print("In valid choice")
