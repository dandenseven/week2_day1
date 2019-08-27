class Person:

    class_attribute = "this is a class attribute"

    def __init__(self, name):
        self.name = name
        # self.height = height
        # self.something_else = something_else

    def introduce(self):
        print("Hi, my name is {}".format(self.name))

    def test(self):
        print("person")

    def make_noise(self):
        self.introduce()

greg = Person("Greg")
greg.introduce()
dane = Person("Dane")
dane.introduce()
john = Person("John")
john.introduce()

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        # self.name = name
        self.subject = subject

    def introduce(self):
        print("Hi, my name is {} and I teach {}".format(self.name, self.subject))

greg = Teacher("Greg", "Web Developement")
greg.introduce()

class Animal:

    def make_noise(self):
        print("Awwooooooo")

class Werewolf(Animal, Person):
    pass

werewolf = Werewolf("Greg")
werewolf.make_noise()
print(werewolf.name)
