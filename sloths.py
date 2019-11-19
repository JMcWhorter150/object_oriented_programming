from random import randint
class Sloth:
    def __init__(self, new_name, friendliness=0.5, happiness=10, cuddle_power=3):
        self.name = new_name
        self.friendliness = friendliness
        self.happiness = happiness
        self.cuddle_power = cuddle_power

    def greet(self, whom):
        print(f"Hello, I am {self.name}. Nice to meet you {whom.name}!")
# Make assumption that whatever will be greeted will also have an object name

    def cuddle(self, whom):
        cuddle_chance = randint(0, 10)/10
        if cuddle_chance <= self.friendliness:
            print(f"I cuddle you, {whom.name}")
            whom.happiness += self.cuddle_power
        else:
            print(f"Bad touch, bad touch!")
    
    def receive_toy(self, toy):
        self.toy = toy

    def play_with_toy(self):
        print(f"{self.name} plays with {self.toy.name}")
        self.happiness += self.toy.quality


class SuperSloth(Sloth):
    def __init__(self, new_name):
        super().__init__(new_name, 0.9, 50, 5)

    def cuddle(self, whom):
        # as long as whom has a .name and a .happiness, cuddle method can do its work.
        cuddle_chance = randint(0, 10)/10
        if cuddle_chance <= self.friendliness:
            print(f"I cuddle you, {whom.name}")
            whom.happiness *= self.cuddle_power
        else:
            print(f"Bad touch, bad touch!")

class Toy:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

    

buster = Sloth("Buster")
eric = Sloth("Eric")
jason = SuperSloth("Jason")