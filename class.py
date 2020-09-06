# Python Object-Oriented Programming


class Employee:
    # Class variables
    companyName ="abc"
    totalEmployees = 0
    payRaiseRate = 1.08
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


# Instance of class
emp1 = Employee("Myname", {"unit":"151", "street":"king st n"}, 40, 1000)
emp2 = Employee("TestUser", {"unit":"123", "street":"queen st n"}, 40, 2000)
emp3 = Employee("TestUser", {"unit":"123", "street":"queen st n"}, 40, 3000)

# Create instance using alternative constructor
inpStr = "Jhon Doe-20,queen St N-40-1000"
emp4 = Employee.fromString(inpStr)
print (emp4.__dict__)

# Call the static method
from datetime import date

today = date.today()
print (emp4.runBatchUpload(today))

emp1.applyPayRaise()
emp2.payRaiseRate = 1.05
emp2.applyPayRaise()

Employee.setNewPayRaiseRate(2.05)

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


