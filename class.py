# Python Object-Oriented Programming

# Employee -> Developer, SysOps, DevOps

class Employee:
    # Class variables
    companyName ="abc"
    totalEmployees = 0
    payRaiseRate = 1.03
    payRaiseAmount = 0

    
    # Class Constructor
    def __init__(self, name, address, age, pay):
        # Attributes / instance variables
        self.name = name
        self.address = address
        self.age = age
        self.pay = pay

        self.email = name + "@" + self.companyName + ".com" 
        Employee.totalEmployees = Employee.totalEmployees + 1
        self.empID = Employee.totalEmployees
       
        # print( "Instance:", self.__dict__)

    # Regular instance methods
    def getEmail(self):
        return self.email
    
    def applyPayRaise(self):
        self.pay = int( self.pay * self.payRaiseRate)
        return self.empID
    

    # Class Methods
    @classmethod
    def setNewPayRaiseRate(cls, newPayRaiseRate):
        cls.payRaiseRate = newPayRaiseRate
    # Alternative constructor to pass "Jhon Doe-20,queen St N-40-1000" as constructor
    @classmethod
    def fromString(cls, inpString):
        name, address, age, pay = inpString.split('-')
        return cls(name,address,age,pay)
    # Static method no reference to class ot instances
    @staticmethod
    def runBatchUpload(today):
        # do some work here
        print ("Static method invoked for:",today)
        return True

# SubClass inherited from Employee
class Developer(Employee):
    # Dev Class variables
    payRaiseRate = 1.10

    #Dev Constructor
    def __init__(self, name, address, age, pay, devSpecificAttribute):
        super().__init__(name, address, age, pay)
        # Employee.__init__(self,name,address, age, pay)
        self.devSpecificAttribute = devSpecificAttribute

# SubClass inherited from Employee
class TeamLead(Employee):
    # Dev Class variables
    payRaiseRate = 1.10

    #Dev Constructor
    def __init__(self, name, address, age, pay, employees = None):
        super().__init__(name, address, age, pay)
        # Employee.__init__(self,name,address, age, pay)
        
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    #Add Employee
    def addEmployee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    #Remove Employee
    def removeEmployee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
     #Print Team
    def getTeam(self):
        for emp in self.employees:
            print ("Team:", emp.__dict__)

# Instance of class
emp1 = Employee("FirstEmployee", {"unit":"Area 151", "street":"king st n"}, 40, 1000)
emp2 = Employee("2ndEmp", {"unit":"123", "street":"queen st n"}, 40, 2000)
emp3 = Employee("3rdEmp", {"unit":"123", "street":"queen st n"}, 40, 3000)

# # Create instance using alternative constructor
# inpStr = "Jhon Doe-20,queen St N-40-1000"
# emp4 = Employee.fromString(inpStr)
# print (emp4.__dict__)

dev1 =  Developer("Dev1", {"unit":"555", "street":"king st n"}, 40, 1000, "Python")
dev2 =  Developer("Dev2", {"unit":"Area 51", "street":"king st n"}, 40, 1500, "Java")
dev1.applyPayRaise()
dev2.applyPayRaise()
# print (dev1.__dict__, dev1.payRaiseRate)
# print (dev2.__dict__, dev2.payRaiseRate)

# print(help(Developer))

tl1 =  TeamLead("TL1", {"unit":"Area 51", "street":"king st n"}, 40, 1000, [dev1, dev2])



print(tl1.getTeam())
# Call the static method
# from datetime import date

# today = date.today()
# print (emp4.runBatchUpload(today))

# emp1.applyPayRaise()
# emp2.payRaiseRate = 1.05
# emp2.applyPayRaise()

# Employee.setNewPayRaiseRate(2.05)

# print (Employee.payRaiseRate) 
# print (emp1.payRaiseRate)
# print (emp2.payRaiseRate)
# print (emp3.payRaiseRate)

# print (Employee.__dict__)
# print (emp1.__dict__)
# print (emp2.__dict__)
# print (emp3.__dict__)


# print (emp1.getEmail())
# print (emp2.getEmail())

# print (emp1.totalEmployees)
# print (emp2.empID)
