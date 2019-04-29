
### a class to demonstrate initialization with required arguments, including main function

class LearningUnit():

    uni = "CODE"                        # same for all instances 

    def __init__(self, name, semester): # required on creating instance 
        self.name = name
        self.semester = semester

    def hello_class(self):
        print("Hello", self.name, self.semester, "!")
        return


## test with main function
def main():
    foundations = LearningUnit("Foundations", "SS19")
    foundations.hello_class()

if __name__ == "__main__":
    main()
