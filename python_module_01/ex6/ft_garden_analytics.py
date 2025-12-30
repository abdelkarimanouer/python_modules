class Plant:
    """Blueprint for making plant objects"""
    type = "regular"

    def __init__(self, name: str, height: int) -> None:
        """Setup plant with name, height"""
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def report(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Plant that has flowers with color and blooming status"""
    type = "flowering"

    def __init__(self, name: str, s_height: int, color: str,
                 is_blooming: bool) -> None:
        super().__init__(name, s_height)
        self.color = color
        self.is_blooming = is_blooming

    def report(self) -> str:
        if self.is_blooming:
            return f"{super().report()}, {self.color} flowers (blooming)"
        else:
            return f"{super().report()}, {self.color} flowers (not blooming)"


class PrizeFlower(FloweringPlant):
    """Special flowering plant that can win prizes"""
    type = "prize flowers"

    def __init__(self, name: str, s_height: int, color: str,
                 is_blooming: bool, prize_points: int) -> None:
        super().__init__(name, s_height, color, is_blooming)
        self.prize_points = prize_points

    def report(self) -> str:
        return f"{super().report()}, Prize points: {self.prize_points}"


class GardenManager:
    """Manager for handling gardens with plants and statistics"""
    class GardenStats:
        """Helper class to calculate garden statistics"""
        def calculate_stats(self, plants, total_growth):
            regular_count = 0
            flowering_count = 0
            prize_count = 0
            for plant in plants:
                if plant.type == "regular":
                    regular_count += 1
                elif plant.type == "flowering":
                    flowering_count += 1
                elif plant.type == "prize flowers":
                    prize_count += 1
            print(f"Plants added: {len(plants)}, Total growth: "
                  f"{total_growth}cm")
            print(f"Plant types: {regular_count} regular, {flowering_count} "
                  f"flowering, {prize_count} prize flowers")

    total_gardens = 0

    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name
        self.plants = []
        self.total_growth = 0
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls, owner_names: list[str]):
        gardens = []
        for name in owner_names:
            garden = cls(name)
            gardens.append(garden)
        return gardens

    @staticmethod
    def validate_height(height: int) -> bool:
        if height > 0:
            return True
        else:
            return False

    def add_plant(self, plant: Plant, showed: bool = True):
        self.plants.append(plant)
        if showed:
            print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all(self):
        print(f"\n{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def report(self):
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"{plant.report()}")
        print()
        stats = self.GardenStats()
        stats.calculate_stats(self.plants, self.total_growth)


if __name__ == "__main__":
    """Main program starts here"""

    print("=== Garden Management System Demo ===\n")
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", True, 10)

    alice, bob = GardenManager.create_garden_network(["Alice", "Bob"])

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    alice.grow_all()
    alice.report()

    tree = Plant("Pine", 60)
    flower = FloweringPlant("Lily", 32, "white", False)

    print()
    bob.add_plant(tree, False)
    bob.add_plant(flower, False)

    print()
    print(f"Height validation test: {GardenManager.validate_height(25)}")
    oak.height = 141
    alice_score = sum(plant.height for plant in alice.plants)
    bob_score = sum(plant.height for plant in bob.plants)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")
