class Employee:
    raise_pay = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' +last + '@company.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last 

    @fullname.deleter
    def fullname(self):
        print('deleted')
        self.first = None
        self.last = None

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    # def __repr__(self):
    #     return 'Employee({}, {}, {})'.format(self.first,self.last,self.email(),self.fullname())

emp1 = Employee('yashwanth','selva ganesh',500000)
emp2 = Employee('yashwanth2','selva ganesh2',500000)


emp1.fullname = 'vishaali sureshkumar'
print(emp1.first)
print(emp1.email)
print(emp1.fullname)

# print(emp1)

del emp1.fullname
print(emp1.first) 