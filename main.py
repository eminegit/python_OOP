#Create a class named MyDog and define the following properties
#Instance attributes: breed, name, age, color, isAsleep=False
#__init__ method that takes breed, name, age, color as parameters, sets the
#values for them and also sets isAsleep to False
#instance methods:
#▶ walk() which prints "name is walking!"
#▶ eat(food) which prints "name is eating food!"
#▶ sleep() which changes the value of the instance attribute, isAsleep to True and  prints "name is sleeping!"
#▶ wake_up() which changes the value of the instance attribute, isAsleep to False and prints "name is waking up!"
#▶ info() which prints out the values for all instance attributes except isAsleep

class MyDog:
    def __init__(self,breed, name, age, color):
        self.breed = breed
        self.name = name
        self.age = age
        self.color = color


    def walk(self):
        print(f"{self.name} is walking!")

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        self.isAsleep = True
        print(f"{self.name} is sleeping")
    def wake_up(self):
        self.isAsleep = False
        print(f"{self.name} is waking up")



dog1 = MyDog("poodle", "kitkat", 3, "white")
dog1.walk()
dog1.eat()
dog1.sleep()
dog1.wake_up()

# This is the changes I made in the feature branch

