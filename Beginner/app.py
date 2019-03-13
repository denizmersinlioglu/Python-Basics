from Student import Student
from GraduateStudent import GraduateStudent

student1 = Student("Jim", "Bussines", 2.3, False)
student2 = Student("deniz", "EE", 2.2, True)

gradute = GraduateStudent("Asim", "PHYS", 4, False)

print(student1.gpa)
print(student1.read_book())
print(gradute.read_book())
print(gradute.write_book())
