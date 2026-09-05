from datetime import datetime

class Frodo:
    def __init__(self):
        self.eating_time = []
        self.pooping_time = []

    def to_eat(self):
        self.eating_time.append(datetime.now().strftime("%H:%M"))

    def to_poop(self):
        self.pooping_time.append(datetime.now().strftime("%H:%M"))

    def statistics(self):
        return {
            "eating_time": self.eating_time,
            "pooping_time": self.pooping_time
        }

frodo = Frodo()
frodo.to_eat()
frodo.to_poop()
print(frodo.statistics())