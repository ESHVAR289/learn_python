# Python OOPS
class Employee:
    raise_amount = 1.05

    def __init__(self, first_name, last_ame, email, age, salary):
        self.first_name = first_name
        self.last_name = last_ame
        self.age = age
        self.salary = salary
        self.email = email

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
