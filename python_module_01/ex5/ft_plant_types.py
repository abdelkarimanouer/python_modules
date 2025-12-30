class Plant:
    """Blueprint for making plant objects"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Setup plant with name, height and age"""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Flower plant that can bloom with color"""
    def __init__(self, name: str, s_height: int, s_age: int,
                 color: str) -> None:
        super().__init__(name, s_height, s_age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Tree plant that has trunk and makes shade"""
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = 3.14 * (self.trunk_diameter / 10) ** 2
        print(f"{self.name} provides {int(shade)} square meters of shade")


class Vegetable(Plant):
    """Vegetable plant with harvest time and nutrition info"""
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    """Main program starts here"""

    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 15, "yellow")
    print(f"\n{rose.name} (Flower): {rose.height}cm, {rose.age} days, "
          f"{rose.color} color")
    rose.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 400, 1000, 40)
    print(f"\n{oak.name} (Tree): {oak.height}cm, {oak.age} days, "
          f"{oak.trunk_diameter}cm diameter")
    oak.produce_shade()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 60, "fall", "vitamin A")
    print(f"\n{tomato.name} (Vegetable): {tomato.height}cm, "
          f"{tomato.age} days, {tomato.harvest_season} harvest")
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")
