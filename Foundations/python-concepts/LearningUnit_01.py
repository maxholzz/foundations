
### a class to demonstrate initialization with required arguments 

class LearningUnit():

    uni = "CODE"                        # same for all instances 

    def __init__(self, name, semester): # required on creating instance 
        self.name = name
        self.semester = semester

    def hello_class(self):
        print("Hello", self.name, self.semester, "!")
        return


## test 
foundations = LearningUnit("Foundations", "SS19")
foundations.hello_class()

web_design = LearningUnit("Responsive Web Design", "SS19")
web_design.hello_class()
