class Plant:
    """Blueprint for making plant objects"""
    total_plants = 0

    def __init__(self, name: str, s_height: int, s_age: int) -> None:
        """Setup plant with name, height and age"""
        self.name = name
        self.height = s_height
        self.age = s_age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")
        Plant.total_plants += 1


if __name__ == "__main__":
    """Main program starts here"""

    print("=== Plant Factory Output ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Oak", 200, 365)
    p3 = Plant("Cactus", 5, 90)
    p4 = Plant("Sunflower", 80, 45)
    p5 = Plant("Fern", 15, 120)
    print(f"\nTotal plants created: {Plant.total_plants}")
