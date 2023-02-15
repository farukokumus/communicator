# this ex is about classess and object
from human import Human
from student import Student

human1= Human("Faruk", 25)
student1= Student(3.25,"eng",human1.name,human1.age)




def main():
    human1.printName()
    student1.printName()
    student1.changeMajor("bus")
    student1.printMajor()
    print(student1)

if __name__== main():
    main()


