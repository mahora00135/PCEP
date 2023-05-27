class Student:
    name = 'fateme'
    def score(self, x, y, z):
        s = (x + y + z) / 3
        return s




myStudent = Student()
result = myStudent.name
#myStudent.name = 'Amin'
result = myStudent.score(19, 20 , 18)
print(result)




myStudent2 = Student()
myStudent2.name = 'ali'
result = myStudent2.score(10, 15, 20)
print(result)