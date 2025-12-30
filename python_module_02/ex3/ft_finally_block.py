def water_plants(plant_list):
    """Water all plants and clean up system."""
    success = False
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise Exception("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
        success = True
    except Exception as e:
        print("Error:", e)
        success = False
    finally:
        print("Closing watering system (cleanup)")
        if success:
            print("Watering completed successfully!")


def test_watering_system():
    """Test watering with good and bad inputs."""
    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])

    print("\nTesting with error...")
    water_plants(["tomato", None])


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
