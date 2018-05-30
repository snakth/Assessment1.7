import requests


class Animals:
    head = 1
    body = 1
    legs = 4
    wings = 2

    coordinates = 0

    def __init__(self, coordinates):
        self.coordinates = coordinates


class Mammals(Animals):
    wings = 0
    horns = "yes"


class Cow (Mammals):
    sound = "mooo"


class Goat(Mammals):
    sound = "baa"


class Sheep(Mammals):
    sound = "baa"


class Pig(Mammals):
    horns = "no"
    sound = "oink"


class Birds(Animals):
    legs = 2


class Duck(Birds):
    sound = "quack"


class Chicken(Birds):
    sound = "cluck"


class Goose(Birds):
    sound = "cackle"


cow_0 = Cow(2)
goat_0 = Goat(5)
sheep_0 = Sheep(1)
pig_0 = Pig(4)

duck_0 = Duck(15)
chicken_0 = Chicken(10)
goose_0 = Goose(13)
