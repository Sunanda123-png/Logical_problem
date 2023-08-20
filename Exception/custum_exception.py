class SalaryNotInRange(Exception):
    def __init__(self, salary, message='Salary not in range'):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter the number between 200 to 600 :- "))
if not 200 < salary < 600:
    raise SalaryNotInRange(salary)
