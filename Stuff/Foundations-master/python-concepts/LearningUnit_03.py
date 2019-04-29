
### a class to demonstrate getter and setter methods

class LearningUnit():

    uni = "CODE"                        # same for all instances 

    def __init__(self, name, semester): # required on creating instance 
        self.name = name
        self.semester = semester

        # create default null value for non-required variables
        self.number_students = None 

    def hello_class(self):
        print("Hello", self.name, self.semester, "!")
        return

    # example setter
    def set_number_students(self,value):
        self.number_students = value

    # example getter 
    def get_number_students(self):
        return self.number_students


## test with main function
def main():
    foundations = LearningUnit("Foundations", "SS19")
    foundations.hello_class()
    foundations.get_number_students() # doesn't crash, but returns null 
    foundations.set_number_students(49) # set the value  
    foundations.get_number_students()  # doesn't crash, but returns null


if __name__ == "__main__":
    main()
