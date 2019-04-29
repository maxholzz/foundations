
### a simple demonstration class 
### usage: open python REFL in directory with file 
### within the REFL: 
### >>> from LearningUnit import LearningUnit
### >>> foundations = LearningUnit()
### >>> foundations.hello_class()

class LearningUnit():
    name = "Founations"
    semester = "SS19"

    def hello_class(self):
        print("Hello", self.name)
        return

### test 
foundations = LearningUnit() # create an object, which is an instance of the class 
foundations.hello_class()()           # call a method on the object 
