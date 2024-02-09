import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.thirst = 50
        self.gladness = 50
        self.alive = True

    def to_eat(self):
        print("Eat something!")
        kushatb = random.randint(1,2)
        if kushatb == 1:
            print("You ate a rat!")
            self.hunger -= 5
        if kushatb == 2:
            print("You ate a kitkat!")
            self.hunger += 5
    def to_drink(self):
        print("Drink something!")
        pitb = random.randint(1,2)
        if pitb == 1:
            print("You drink from air conditioner!")
            self.thirst -= 5
        if pitb == 2:
            print("You drink from miska!!!!")
            self.thirst += 5

    def to_sleep(self):
        print("Go sleep!")
        spatb = random.randint(1,2)
        if spatb == 1:
            print("You sleep in a garage!")
            self.gladness -= 5
        if spatb == 2:
            print("You sleep in a bedroom!")
            self.gladness += 5

    def is_alive(self):
        if self.hunger <= 0:
            print("You dead from a hunger!")
            self.alive = False
        elif self.gladness <= 0:
            print("You felt sleeping for an eternity")
            self.alive = False
        elif self.thirst <= 0:
            print("You dead from a thirstness")
            self.alive = False

    def end_of_day(self):
        print(f"Hunger = {self.hunger}")
        print(f"Thirst = {self.thirst}")
        print(f"Gladness = {self.gladness}")

    def live(self, day):
        d = f"Day {day} of {self.name} life "
        print(f"{d:=^25}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_drink()
        elif live_cube == 3:
            self.to_sleep()
        self.end_of_day()
        self.is_alive()




simon = Cat("Simon")
for day in range(1, 366):
    if simon.alive == False:
        break
    simon.live(day)