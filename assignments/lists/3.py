(lst := input("Enter list separated by commas: ").split(",")) and print([x for x in lst if lst.count(x) == 1])