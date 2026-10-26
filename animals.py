class Animal:
    def __init__(self):
        pass
    def speak(self):
        return "speak"
def Dog(Animal):
    def __init__(self):
        Animal.__init__()
        pass
    def speak(self):
        return "Bark"
def Cat(Animal):
    def __init__(self):
        Animal.__init__()
        pass
    def speak(self):
        return "Meow"