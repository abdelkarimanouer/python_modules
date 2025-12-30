def check_temperature(temp_str: str):
    """Check if temperature is safe for plants (0-40°C)."""
    try:
        number = int(temp_str)
        if number > 40:
            print(f"Error: {number}°C is too hot for plants (max 40°C)")
        elif number < 0:
            print(f"Error: {number}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {number}°C is perfect for plants!")
            return (number)
    except Exception:
        print(f"Error: \'{temp_str}\' is not a valid number")


def test_temperature_input():
    """Test temperature checker with different values."""
    mytests = ["25", "abc", "100", "-50"]
    i = 0
    while i < 4:
        print("\nTesting temperature: " + mytests[i])
        check_temperature(mytests[i])
        i += 1
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature_input()
