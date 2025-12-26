class Employee:
    raise_percentage = 1.04

    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def raise_pay(self):
        self.pay = int(self.pay * self.raise_percentage)

class Developer(Employee):
    raise_percentage = 1.1
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        # Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang

dev1 = Developer('Yashwanth', 'Selva Ganesh', 20000, 'Python')
dev2 = Developer('Ya', 'S', 20000, 'Java')

print(dev1.email)
print(dev1.prog_lang)   