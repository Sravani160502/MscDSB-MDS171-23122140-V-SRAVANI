class studentdetails:
     def __init__ (self):
          self.dict = { }
     def storestudent_details(self,UID,Name,email,PythonProgramming,AppliedExcel,ResearchMethodology,Mathematics,Statistics):
          temp = {"Uid" : UID,
                   "name" :Name ,
                   "Gmail" : email , 
                   "Programming":PythonProgramming,
                   "excel": AppliedExcel,
                   "Research":ResearchMethodology,
                   "Maths":Mathematics,
                   "Stats":Statistics
                   }
          self.dict[UID,Name,email,PythonProgramming,AppliedExcel,ResearchMethodology,Mathematics,Statistics] = temp
     
     def printdetails(self):
         print(self.dict)
     
     def viewdetails(self):
         for item in self.dict:
             print(item)
         
def add_details():
    UID = int(input("enter the Id"))
    Name = input("enter the name")
    email= input("enter the email")
    PythonProgramimmg= int(input("enter the python marks"))
    AppliedExcel = int(input("enter the excel marks"))
    ResearchMethodology = int(input("enter the RM marks"))
    Mathematics = int(input("enter the Mathsmarks"))
    Statistics= int(input("enter the statsmarks"))
    return UID,Name,email,PythonProgramimmg,AppliedExcel,ResearchMethodology,Mathematics,Statistics  
     
students = studentdetails()

classdetails = open("classdetails.csv")
classdetails_headers = classdetails.readline()
classdetails_details = classdetails.readlines()

for item in classdetails_details:
     temp = item.strip().split(',')
     students.storestudent_details(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7])
students.printdetails()