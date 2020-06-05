class Animal():
    def __init__(self, species=None):
        if species is None:
            self._species = "NA"
        else:
            self._species = species
        self._color = "NA"
        self._name = "NA"

    def noise(self):  # Abstract method: too specific
        pass        # to be implemented here

    def eat(self):  # Abstract method: too specific
        pass      # to be implemented here

    def set_color(self, value):
        self._color = value

    def get_color(self):
        return self._color

    def set_name(self, value):
        self._name = value

    def get_name(self):
        return self._name

    def set_species(self, value):
        self._species = value

    def get_species(self):
        return self._species

    def __str__(self):
        return "%s is a %s %s" % (self._name, self._color, self._species)
