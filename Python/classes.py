class Employee:
    number_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first + '.' + last + '@company.com').lower()
        Employee.number_of_emp += 1

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime
my_date = datetime.date(2021, 1, 24)

emp_1 = Employee('Anton', 'Brahar', 1000)
emp_2 = Employee('Denis', 'Arkusha', 4000)
emp_3 = Employee('Tony', 'Chavez', 2000)

print(Employee.number_of_emp)
print(emp_1.email, emp_1.pay)
print(emp_2.email)
print(emp_2.is_workday(my_date))


