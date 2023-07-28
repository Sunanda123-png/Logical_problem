"""Write a Python function student_data () that will print the ID of a student (student_id). If the user passes
an argument student_name or student_class the function will print the student name and class."""


class Student:
    def __init__(self, student_id):
        self.student_id = student_id

    def student_data(self, *args, **kwargs):
        print(args)
        print(kwargs)
        print(f'student_id: {self.student_id}')
        if 'student_name' in kwargs:
            print(f'student_name:{kwargs["student_name"]}')


obj = Student(101)
obj.student_data("45678", student_name="Rahul")
