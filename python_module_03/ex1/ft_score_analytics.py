import sys

if __name__ == "__main__":
    try:
        print("=== Player Score Analytics ===")
        if len(sys.argv) > 1:
            mylist = []
            for e in sys.argv[1:]:
                mylist.append(int(e))
            total_number = len(mylist)
            sum_numbers = sum(mylist)
            max_number = max(mylist)
            min_number = min(mylist)
            print("Scores processed:", mylist)
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
