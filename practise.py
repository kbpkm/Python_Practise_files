class Employee:

    raise_amount = 4

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first +  last + '09' + '@gmail.com'
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay =int(self.pay * self.raise_amount)


emp_1 = Employee('Abhishek', 'Gaddam', 600000)
print(Employee.raise_amount)
print(emp_1.raise_amount)
    


