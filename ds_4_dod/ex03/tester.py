from new_student import Student


student = Student(name="Edward", surname="agle")
print("-------------Before change active......................")
print(student)
print(student.__dict__)
student.active = False
print("-------------after change active......................")
print(student)
print(student.__dict__)


student = Student("agle", "Edward")
print(student)


student = Student(name="", surname="agle")
print(student)
student = Student(name="Edward", surname="agle", id="toto")
print(student)
