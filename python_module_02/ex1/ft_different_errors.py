def garden_operations(type: str):
    """Show different types of errors and how to catch them."""
    if type == "ValueError":
        try:
            x = int("invalid input")
            x = x + 5
        except ValueError:
            print("Caught ValueError: invalid literal for int()")
    elif type == "ZeroDivisionError":
        try:
            y = 9 / 0
            y = y + 5
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
    elif type == "FileNotFoundError":
        try:
            with open("non_exist.txt", "r"):
                pass
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'")
    elif type == "KeyError":
        try:
            my_dict = {"name": "Alice", "age": 25}
            v = my_dict["bob"]
            print(v)
        except KeyError:
            print("Caught KeyError: \'missing\\_plant\'")
    elif type == "multiple":
        try:
            x = int("abc")
            y = 9 / 0
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Caught an error, but program continues!")


def test_error_types():
    """Test all different error types."""
    print("\nTesting ValueError...")
    garden_operations("ValueError")

    print("\nTesting ZeroDivisionError...")
    garden_operations("ZeroDivisionError")

    print("\nTesting FileNotFoundError...")
    garden_operations("FileNotFoundError")

    print("\nTesting KeyError...")
    garden_operations("KeyError")

    print("\nTesting multiple errors together...")
    garden_operations("multiple")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
