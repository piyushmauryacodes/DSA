class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.pin=pin
        self.salary=salary


Piyush=Programmer("Piyush",12000000,221106)
print(Piyush.salary,Piyush.company,Piyush.name,Piyush.pin)