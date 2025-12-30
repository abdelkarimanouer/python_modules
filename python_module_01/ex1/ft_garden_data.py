class Plant:
    """Blueprint for making plant objects"""
    def __init__(self) -> None:
        """Setup empty plant with no values yet"""
        self.name: str
        self.height: int
        self.age: int


if __name__ == "__main__":
    """Main program starts here"""

    p1 = Plant()
    p2 = Plant()
    p3 = Plant()

    p1.name = "Rose"
    p1.age = 30
    p1.height = 25

    p2.name = "Sunflower"
    p2.age = 45
    p2.height = 80

    p3.name = "Cactus"
    p3.age = 120
    p3.height = 15

    print("=== Garden Plant Registry ===")
    print(f"{p1.name}: {p1.height}cm, {p1.age} days old")
    print(f"{p2.name}: {p2.height}cm, {p2.age} days old")
    print(f"{p3.name}: {p3.height}cm, {p3.age} days old")
