class Plant:
    """Blueprint for making plant objects"""
    def __init__(self) -> None:
        """Setup empty plant with no values yet"""
        self.name: str
        self.height: int
        self.days: int

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1

    def get_info(self) -> str:
        """Return plant info as string"""
        return f"{self.name}: {self.height}cm, {self.days} days old"


if __name__ == "__main__":
    """Main program starts here"""

    p1 = Plant()
    p1.name = "Rose"
    p1.days = 30
    p1.height = 25
    old_height = p1.height
    print("=== Day 1 ===")
    print(p1.get_info())
    for i in range(6):
        p1.grow()
        p1.age()
    print("=== Day 7 ===")
    print(p1.get_info())
    growth = p1.height - old_height
    print(f"Growth this week: +{growth}cm")
