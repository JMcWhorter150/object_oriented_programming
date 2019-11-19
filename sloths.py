class Sloth:
    def __init__(self, new_name):
        self.name = new_name

    def greet(self, whom):
        print(f"Hello, I am {self.name}. Nice to meet you {whom.name}!")
# Make assumption that whatever will be greeted will also have an object name

    def cuddle(self, whom):
        pass

othersloth = Sloth("Buster")
mysloth = Sloth("Eric")