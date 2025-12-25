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
        
    @classmethod
    def change_raise(cls,percentage):
        cls.raise_pay = percentage

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp1 = Employee('yashwanth','selva ganesh',500000)
emp2 = Employee('yashwanth2','selva ganesh2',500000)


emp_str_1 = 'yash-wanth-2000'
emp_str_2 = 'yashwa-dev-2000'
emp_str_3 = 'hello-yash-2000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)


# first, last, pay = emp_str_1.split('-')
# emp3 = Employee(first,last,pay)
# print(emp3.first,emp3.last,emp3.pay)

Employee.change_raise(1.05)

print(emp1.apply_raise())
print(emp2.apply_raise())