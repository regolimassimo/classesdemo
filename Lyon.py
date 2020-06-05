import random
from Animal import Animal


class Lyon(Animal):
    ALLOWED_COLORS = ["BROWN", "LIGHT BROWN", "CHESTNUT",
                      "OCHRE", "CINNAMON", "WHITE"]

    def __init__(self):
        Animal.__init__(self, species="Leo")

    def set_color(self, value):
        if value not in self.ALLOWED_COLORS:
            raise Exception("BAD COLOR")
        else:
            Animal.set_color(self, value)

    def noise(self):
        print("ROAR!")

    def eat(self):
        print("RAW MEAT")

    def mix(self, col1, col2):
        if col1 == col2: # geni uguali
            return col1
        if col1 == "WHITE": # recessivo
            return col2
        if col2 == "WHITE": # recessivo
            return col1
        if col1 == "BROWN" or col2 == "BROWN": #dominante
            return "BROWN"
        n = random.randint(0, len(self.ALLOWED_COLORS))
        return self.ALLOWED_COLORS[n]


    def set_color(self, value):
        if value not in self.ALLOWED_COLORS:
            raise Exception("BAD COLOR")
        else:
            Animal.set_color(self, value)

    def __add__(self, other):
        son = Lyon()
        col1 = self.get_color()
        col2 = other.get_color()
        color = self.mix(col1, col2)
        son.set_color(color)
        son.set_name("SON OF %s AND %s" %
                     (self.get_name(), other.get_name()))
        return son

    def noise(self):
        print("ROAR!")
