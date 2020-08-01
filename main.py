from oops import Employee

if __name__ == '__main__':
    emp1 = Employee('Eshvar', 'Mali', 'eshvar289@gmail.com', 27, 50000)
    emp2 = Employee('Sagar', 'Lohar', 'sagar.lohar@gmail.com', 27, 52000)
    emp3 = Employee('Rahul', 'Thorat', 'rahul.thorat@gmail.com', 27, 55000)

    print(emp1.full_name())
    print('before raise salary : ' + str(emp1.salary))
    emp1.apply_raise()  # raise emp1 salary
    print('after raise salary : ' + str(emp1.salary))
