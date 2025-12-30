class Plant:
    """
    A simple plant with basic information.
    Stores name, water level, and sunlight hours.
    """
    def __init__(self, plant_name, water_level, sunlight_hours) -> None:
        """Initialize with needed values."""
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenError(Exception):
    """
    Basic error for any garden problem.
    Parent class for all garden errors.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    """
    Error for plant-specific problems.
    Like empty name or invalid plant.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    """
    Error for water-related problems.
    Like too much or too little water.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)


class GardenManager:
    """
    Manages a garden with plants.
    Can add plants, water them, and check their health.
    """
    def __init__(self) -> None:
        """Initialize with needed values."""
        self.plants = []
        self.tank = 15

    def check_plant_health(self):
        """
        Check if each plant is healthy.
        Checks water level and sunlight hours.
        Raises error if something is wrong.
        """
        for p in self.plants:
            try:
                if p.plant_name == "" or p.plant_name is None:
                    raise PlantError("Plant name cannot be empty!")
                elif p.water_level < 1 or p.water_level > 10:
                    if p.water_level < 1:
                        raise WaterError(f"Water level {p.water_level} "
                                         f"is too low (min 1)")
                    else:
                        raise WaterError(f"Water level {p.water_level} "
                                         f"is too high (max 10)")
                elif p.sunlight_hours < 2 or p.sunlight_hours > 12:
                    if p.sunlight_hours < 2:
                        raise GardenError(f"Sunlight hours {p.sunlight_hours}"
                                          f" is too low (min 2)")
                    else:
                        raise GardenError(f"Sunlight hours {p.sunlight_hours}"
                                          f" is too high (max 12)")
                else:
                    print(f"{p.plant_name}: healthy "
                          f"(water: {p.water_level}, sun: {p.sunlight_hours})")
            except (PlantError, WaterError, GardenError) as e:
                print(f"Error checking {p.plant_name}:", e)

    def add_plant(self, plant_name, water_level, sunlight_hours):
        """
        Add a new plant to the garden.
        Raises PlantError if name is empty.
        """
        try:
            if plant_name == "" or plant_name is None:
                raise PlantError("Plant name cannot be empty!")
            else:
                p = Plant(plant_name, water_level, sunlight_hours)
                self.plants.append(p)
                print(f"Added {plant_name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        """
        Water all plants in the garden.
        Opens system, waters plants, then closes system.
        Always closes system even if error happens.
        """
        success = False
        try:
            print("Opening watering system")
            for plant in self.plants:
                if plant is None:
                    raise WaterError("Cannot water None - invalid plant!")
                print(f"Watering {plant.plant_name} - success")
                plant.water_level += 5
            success = True
        except WaterError as e:
            print("Error:", e)
            success = False
        finally:
            print("Closing watering system (cleanup)")
            if success:
                print("Watering completed successfully!")

    def check_tank(self):
        """
        Check if water tank has enough water.
        Raises GardenError if tank is too low.
        Shows that program recovers from error.
        """
        try:
            if self.tank < 20:
                raise GardenError("Not enough water in tank")
        except GardenError as e:
            print("Caught GardenError:", e)
        print("System recovered and continuing...")


if __name__ == "__main__":
    print("=== Garden Management System ===")

    print("\nAdding plants to garden...")
    manager = GardenManager()
    manager.add_plant("tomato", 0, 8)
    manager.add_plant("lettuce", 10, 4)
    manager.add_plant(None, 4, 8)

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_plant_health()

    print("\nTesting error recovery...")
    manager.check_tank()

    print("\nGarden management system test complete!")
