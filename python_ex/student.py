from human import Human

class Student(Human):
    def __init__(self, gpa, major, name, age):
        self.gpa=gpa
        self.major= major
        super().__init__(name,age)
        #self.name = name
        #self.age= age

    def __str__(self):
        return f"Studen name is " + self.name + " and its major is " + self.major     

    def printName(self):
        print("Students name is ")
        super().printName() 
    def printMajor(self):
        print("Students major is" + self.major)


    def changeMajor(self,newmajor):
        self.major=newmajor