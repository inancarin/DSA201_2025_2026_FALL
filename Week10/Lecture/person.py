class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name: " + self.name + ", and age:" + str(self.age)
    
    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name
    
class Student(Person):
    def __init__(self, name, age, school):
        """
        self.name = name
        self.age = age
        """
        super().__init__(name, age)
        self.school = school
    
    def getSchool(self):
        return self.school
   
    def __str__(self):
        return super().__str__() + ", school: " + self.school

class Doctor(Person):
    def __init__(self, name, age, hospital):
        super().__init__(name, age)
        self.hospital = hospital
    
    def __str__(self):
        return "Dr. " + super().getName() + " from " + self.hospital


class UniversityStudent(Student):
    pass

class HighSchoolStudent(Student):
    pass

if __name__ == "__main__":
    p1 = Person("John", 23)
    p2 = Person("Alice", 18)
    print(p1)
    print(p2)

    s1 = Student("Jack", 19, "Stanford University")
    print(s1.getName())
    print(s1)

    d1 = Doctor("Ahmet", 45, "Acibadem Hospital")
    print(d1)