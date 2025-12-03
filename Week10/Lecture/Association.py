from person import Person

class FaculyMembers(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.empID = id
        self.teachingCourses = []
    
    def teachCourse(self, c): # c is an instance of Course class
        if c not in self.teachingCourses:
            self.teachingCourses.append(c)
    
    def printAllTeachingCourses(self):
        if len(self.teachingCourses) == 0:
            print(self.name, "is not teaching yet")
        else:
            print("Here is the courses for instructor", self.name)
            for c in self.teachingCourses:
                print(c)

class Student(Person):
    def __init__(self, name, age, studentID, university):
        super().__init__(name, age)
        
        self.studenID = studentID
        self.univesity = university
        self.courses = []
    
    def printAllCourses(self):
        if len(self.courses) == 0:
            print("Student has not taken any course yet")
        else:
            print("Here is the courses taken by student", self.studenID)
            for c in self.courses:
                print(c)

    def register(self, c): # c is an instance of Course class
        if c not in self.courses:
            if not c.isFull():
                self.courses.append(c)
                c.cur_population += 1
                c.students.append(self)
                print("Enrollment was successful for student", self.studenID, "into course", c.code)
            else:
                print("The course is full, you cannot register!")
        else:
            print("You have already registered this course")

class Course:
    def __init__(self, CRN, code, capacity):
        self.CRN = CRN
        self.code = code
        self.capacity = capacity
        self.cur_population = 0
        self.students = []
    
    def __str__(self):
        return str(self.CRN)+ ", " + self.code

    def printAllStudents(self):
        if len(self.students) == 0:
            print("No student has register to the course")
        else:
            print("Here is the list of the students:")
            for s in self.students:
                print(s)
    
    def isFull(self):
        if self.capacity > self.cur_population:
            return False
        return True
    
    def changeCapacity(self, newCapacity):
        self.capacity = newCapacity
    
if __name__ == "__main__":
    s1 = Student("John", 21, 10, "Sabanci University")
    s2 = Student("Jack", 20, 11, "Sabanci University")
    s3 = Student("Alice", 21, 12, "Sabanci University")

    if100 = Course(25345, "if100", 3)
    dsa201 = Course(24555, "dsa201", 2)

    s1.printAllCourses()
    s1.register(dsa201)
    s2.register(dsa201)
    s3.register(dsa201) # was not succs
    s1.register(if100)
    s2.register(if100)
    s3.register(if100)
    dsa201.changeCapacity(4)
    s3.register(dsa201) # succs

    s1.printAllCourses()

    if100.printAllStudents()

    f1 = FaculyMembers("Bob", 55, 5)
    f1.printAllTeachingCourses()
    f1.teachCourse(dsa201)
    f1.teachCourse(if100)
    f1.printAllTeachingCourses()