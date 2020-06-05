from Animal import Animal
from Lyon import Lyon

animal = Animal()

leo = Lyon()
leo.set_color("BROWN")


leo.set_name("SIMBA")
# leo.eat()
# print(leo)

leo1 = Lyon()
leo1.set_name("SIMBA")
leo1.set_color("WHITE")
leo2 = Lyon()
leo2.set_name("NALA")
leo2.set_color("LIGHT BROWN")
leo3 = leo1 + leo2
print(leo1)
print(leo2)
print(leo3)