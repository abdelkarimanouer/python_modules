import sys

if __name__ == "__main__":
    try:
        print("=== Player Score Analytics ===")
        mylist = sys.argv[1:]
        total_number = len(mylist)
        if total_number >= 1:
            sum_numbers = sum(mylist)
            max_number = max(mylist)
            min_number = min(mylist)
            print("Total players:", total_number)
            print("Average score:", sum_numbers / total_number)
            print("High score:", max_number)
            print("Low score:", min_number)
            print("Score range:", )
        else:
            print(f"No scores provided. Usage: python3 {sys.argv[0]} "
                  f"<score1> <score2> ...")
    except Exception as e:
        print("Error:", e)
