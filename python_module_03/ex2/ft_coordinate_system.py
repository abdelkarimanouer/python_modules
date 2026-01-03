import math

if __name__ == "__main__":
    try:
        print("=== Game Coordinate System ===")
        pos1 = (0, 0, 0)

        coordinate1 = (10, 20, 5)
        print(f"Position created: {coordinate1}")
        part1 = (pos1[0] - coordinate1[0])**2
        part2 = (pos1[1] - coordinate1[1])**2
        part3 = (pos1[2] - coordinate1[2])**2
        result = math.sqrt(part1 + part2 + part3)
        print(f"Distance between {pos1} and {coordinate1}: {result:.2f}")

        str_coordinate2 = "3,4,0"
        print(f"Parsing coordinates: {str_coordinate2}")
        coordinate2 = tuple(int(n) for n in str_coordinate2.split(","))
        print(f"Parsed position: {coordinate2}")
        part1 = (pos1[0] - coordinate2[0])**2
        part2 = (pos1[1] - coordinate2[1])**2
        part3 = (pos1[2] - coordinate2[2])**2
        result = math.sqrt(part1 + part2 + part3)
        print(f"Distance between {pos1} and {coordinate2}: {result:.2f}")

    except Exception as e:
        print("Error:", e)
