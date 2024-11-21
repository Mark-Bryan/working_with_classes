from student import Student

student = Student("Alex")


student.add_grade(85)
student.add_grade(90)
student.add_grade(78)

print(student.average_grade())

studentAverage = student.average_grade()


print(student.average_grade())
