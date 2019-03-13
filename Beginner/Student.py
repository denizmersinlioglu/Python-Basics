class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def read_book(self):
        print("read book normal")

    def write_book(self):
        print("write book normal")
