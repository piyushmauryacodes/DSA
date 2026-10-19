class Employee:             #This is a classs
    language="Python"       #These are class attributes
    salary=1200000

    def __init__(self,name,salary,language):
        self.name=name       #This is dunder method which is automatically called.
        self.language=language
        self.salary=salary 
        print("i am creating an object")


    def getInfo(self):      #This is a funciton which takes self argument to run a function.
        print(f"The language is {self.language}. The salary is {self.salary}")


    @staticmethod          #This is a static method in which we can call out a function without giving argument in it.
    def greet():
        print("Good Morning Sir...")

piyush=Employee("Piyush",1400000,"Web Developer")
piyush.getInfo()
piyush.greet()
print(piyush.language,piyush.salary)