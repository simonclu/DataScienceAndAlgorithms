class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getAge(self):
        return self.age
    def setAge(self, age):
        self.age = age
class Student(Person):
    def __init__(self, name, age, school):
        super.__init__(name, age)
        self.school = school
        self.division = "preschool" if self.age <= 4 else "lower" if self.age <= 11 else "middle" if self.age <= 14 else "high" if self.age <= 18 else "higher"
        self.grade = "preschool" if self.age <= 3 else "prekindergarten" if self.age <= 4 else "kindergarten" if self.age <= 5 else str(self.age - 5)
    def getSchool(self):
        return self.school
    def setSchool(self, school):
        self.school = school
    def setAge(self, age):
        self.age = age
        self.division = "preschool" if self.age <= 4 else "lower" if self.age <= 11 else "middle" if self.age <= 14 else "high" if self.age <= 18 else "higher"
        self.grade = "preschool" if self.age <= 3 else "prekindergarten" if self.age <= 4 else "kindergarten" if self.age <= 5 else str(self.age - 5)
class Worker(Person):
    def __init__(self, name, age, job, dollarsPerHour):
        super.__init__(name, age)
        self.job = job
        self.dollarsPerHour = dollarsPerHour
    def calculatePay(self, hours):
        return self.dollarsPerHour * hours
    def getJob(self):
        return self.job
    def setJob(self, job):
        self.job = job
    def getDollarsPerHour(self):
        return self.dollarsPerHour
    def setDollarsPerHour(self, dollarsPerHour):
        self.dollarsPerHour = dollarsPerHour