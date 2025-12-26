class Employee:
    raise_pay = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' +last + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_pay)
        return self.pay

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp1 = Employee('yashwanth','selva ganesh',500000)
emp2 = Employee('yashwanth2','selva ganesh2',500000)

print(emp1.__repr__())
print(emp2.__str__())
print(emp1 + emp2)
print(len(emp1))

# print(1 + 2)
# print(int.__sub__(1,2))
# print(str.__add__('a','a'))


