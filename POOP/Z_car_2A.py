class Car: # naming convention: starts with a capital letter
    
    wheels = 4 # class variable, default value, but can be changed when defined in main file

    def __init__(self, make, model, year, color):
        self.make = make    # instance variable
        self.model = model  # instance variable
        self.year = year    # instance variable
        self.color = color  # instance variable

    def drive(self):
        print(f"This {self.model} is driving.")

    def stop(self):
        print(f"This {self.model} has stopped.")
    
    