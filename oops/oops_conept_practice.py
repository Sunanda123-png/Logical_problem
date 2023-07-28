
# class Student:
#
#     def __init__(self,name):
#         self.name = name
#
#     def student_record(self):
#         print(f'{self.name}')
#     @classmethod
#     def student_entry(cls):
#         print("I am a class method")
#
#     @staticmethod
#     def student_sum():
#         pass
#
var =10
def student():
    global var
    var+= 1
    print(var)

print(student())