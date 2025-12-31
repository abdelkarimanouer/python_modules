import sys
if __name__ == "__main__":
    length = len(sys.argv)
    print("=== Command Quest ===")
    if length == 1:
        print("No arguments provided!")
        print("Program name:", sys.argv[0])
    else:
        print("Program name:", sys.argv[0])
        print("Arguments received:", length - 1)
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print("Total arguments:", length)
