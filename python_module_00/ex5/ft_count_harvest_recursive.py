def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    i = 1

    def recurse(days, i):
        if i <= days:
            print("Day", i)
            i += 1
            recurse(days, i)
    recurse(days, i)
