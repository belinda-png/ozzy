class Humanbeing:
    def __init__(self, name, color, sound, size, age):
        self.name = name
        self.color = color
        self.sound = sound
        self.size = size
        self.age = age
    def __str__(self):
        return f"\nHello  Everyone\n my name is {self.name}. \nMy color is {self.color}\n I sound {self.sound}\n I am {self.size} in size\n and I am {self.age} years old."
