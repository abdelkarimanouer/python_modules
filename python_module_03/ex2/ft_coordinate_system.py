import math

if __name__ == "__main__":
    try:
        print("=== Game Coordinate System ===")
        pos1 = (0, 0, 0)

        coordinate1 = (10, 20, 5)
        print(f"\nPosition created: {coordinate1}")
        result = (math.sqrt(
            (pos1[0] - coordinate1[0])**2 +
            (pos1[1] - coordinate1[1])**2 +
            (pos1[2] - coordinate1[2])**2)
        )
        print(f"Distance between {pos1} and {coordinate1}: {result:.2f}\n")

        str_coordinate2 = "3,4,0"
        print(f"Parsing coordinates: \"{str_coordinate2}\"")
        coordinate2 = tuple(int(n) for n in str_coordinate2.split(","))
        print(f"Parsed position: {coordinate2}")
        result = (math.sqrt(
            (pos1[0] - coordinate2[0])**2 +
            (pos1[1] - coordinate2[1])**2 +
            (pos1[2] - coordinate2[2])**2)
        )
        print(f"Distance between {pos1} and {coordinate2}: {result:.1f}\n")

        invalid_coordinate3 = "abc,def,ghi"
        coordinate3 = tuple(int(n) for n in invalid_coordinate3.split(","))

        print("Unpacking demonstration:")
        print(f"Player at x={coordinate2[0]}, y={coordinate2[1]}, "
              f"z={coordinate2[2]}")
        print(f"Coordinates: X={coordinate2[0]}, Y={coordinate2[1]}, "
              f"Z={coordinate2[2]}")

    except Exception as e:
        print("Error parsing coordinates:", e)
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
