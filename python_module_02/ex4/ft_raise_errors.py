def check_plant_health(plant_name, water_level, sunlight_hours):
    """Check if plant values are valid."""
    try:
        if plant_name == "" or plant_name is None:
            raise Exception("Plant name cannot be empty!")
        elif water_level < 1 or water_level > 10:
            if water_level < 1:
                raise Exception(f"Water level {water_level} "
                                f"is too low (min 1)")
            else:
                raise Exception(f"Water level {water_level} "
                                f"is too high (max 10)")
        elif sunlight_hours < 2 or sunlight_hours > 12:
            if sunlight_hours < 2:
                raise Exception(f"Sunlight hours {sunlight_hours} "
                                f"is too low (min 2)")
            else:
                raise Exception(f"Sunlight hours {sunlight_hours} "
                                f"is too high (max 12)")
        else:
            print(f"Plant \'{plant_name}\' is healthy!")
    except Exception as e:
        print("Error:", e)


def test_plant_checks():
    """Test plant health checker with different values."""
    print("\nTesting good values...")
    check_plant_health("tomato", 5, 8)

    print("\nTesting empty plant name...")
    check_plant_health("", 5, 8)

    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 8)

    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 0)


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
    print("\nAll error raising tests completed!")
