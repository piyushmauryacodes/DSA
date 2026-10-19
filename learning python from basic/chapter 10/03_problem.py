class Employee:
    language="Python"
    salary=1200000

    def getInfo(self):
        print(f"The languge is {self.language}. The salary is {self.salary}")

harry = Employee()
harry.language="Javascript" #This is an instance attribute.
harry.getInfo()