class Cats:
    # Initialising my attributes
    def __init__(self, type, name, gender, color, age):
        self.type = type
        self.name = name
        self.gender = gender
        self.color = color
        self.age = age

    def move(self):
        print(
            "I am a : " + self.type + "\n" +
            "My name is : " + self.name + "\n" +
            "My Gender is : " + self.gender + "\n" +
            "My color is: " + self.color + "\n" +
            "My age is : " + self.age)


objCats = Cats("Lion", "White Lion", "Female", "Orange", "5 years old")
objCats.move()


class Lion(Cats):
    pass


class Tiger(Lion):
    pass
