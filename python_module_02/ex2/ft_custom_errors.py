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


def test_plant_error():
    """Test PlantError exception."""
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught {PlantError.__name__}:", e)


def test_water_error():
    """Test WaterError exception."""
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught {WaterError.__name__}:", e)


def test_garden_error():
    """Test that GardenError catches all garden errors."""
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print("Caught a garden error:", e)


def test_errors():
    """Run all error tests."""
    print("\nTesting PlantError...")
    test_plant_error()

    print("\nTesting WaterError...")
    test_water_error()

    print("\nTesting catching all garden errors...")
    test_garden_error()


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_errors()
    print("\nAll custom error types work correctly!")
