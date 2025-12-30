class SecurePlant:
    """Blueprint for making secure plant objects with validation"""
    def __init__(self, name) -> None:
        """Setup plant with name and empty height and age"""
        self.name = name
        self.__height: int
        self.__age: int
        print(f"Plant created: {self.name}")

    def set_height(self, height: int) -> None:
        """Set plant height if value is valid"""
        if (height >= 0):
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height {height}cm "
                  f"[REJECTED]")
            print("Security: Negative height rejected")

    def get_height(self) -> int:
        if (self.__height >= 0):
            """Get plant height safely"""
            return (self.__height)
        else:
            return 0

    def set_age(self, age: int) -> None:
        """Set plant age if value is valid"""
        if (age >= 0):
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"\nInvalid operation attempted: age {age} days "
                  f"[REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self) -> int:
        """Get plant age safely"""
        if (self.__age >= 0):
            return (self.__age)
        else:
            return 0


if __name__ == "__main__":
    """Main program starts here"""

    print("=== Garden Security System ===")
    p1 = SecurePlant("Rose")
    p1.set_height(25)
    p1.set_age(30)
    p1.set_height(-5)
    print(f"\nCurrent plant: {p1.name} ({p1.get_height()}cm, "
          f"{p1.get_age()} days)")
