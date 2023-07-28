class Employee:
    __slots__ = ['_emp_name', '__emp_salary']

    def __init__(self, emp_name, emp_salary):
        self._emp_name = emp_name
        self.__emp_salary = emp_salary


e = Employee("sunaina", 100000)
e._emp_name = "rahul"
e.__emp_salary = 200000
print(e._emp_name)
print(e.__emp_salary)
