def element_practice():
    can_we_count_it = [{'s': False}, "sassafras", 18, ["a", "c", "s", "d", "s"]]

    for element in can_we_count_it:
        if hasattr(element, "count"):
            print(str(type(element)) + " has the count attribute!")
        elif not hasattr(element, "count"):
            print(str(type(element)) + " does not have the count attribute :(")
