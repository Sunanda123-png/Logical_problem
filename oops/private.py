class Student:
    __name = None
    __roll_number = None
    __age = None

    def __init__(self, name, roll_number, age):
        self.__name = name
        self.__roll_number = roll_number
        self.__age = age

    def _student_details(self):
        print(f'{self.__name}')
        print(f'{self.__roll_number}')
        print(f'{self.__age}')

    def display(self):
        return self._student_details()


class School(Student):
    def student_record(self):
        super()._student_details()


obj = School("raj", 205, 14)
obj.student_record()

# student = Student("raj", 101, 15)
# student.display()
