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

class SuperSloth(Sloth):
    def cuddle(self, whom):
        cuddle_chance = randint(0, 10)/10
        if cuddle_chance <= self.friendliness:
            print(f"I cuddle you, {whom.name}")
            whom.happiness *= self.cuddle_power
        else:
            print(f"Bad touch, bad touch!")

buster = Sloth("Buster")
eric = Sloth("Eric")
jason = SuperSloth("Jason")