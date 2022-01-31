def linearsearch(ls, search_el):
    for i, el in enumerate(ls):    # Loop through every single element
        if el == search_el:        # The key comparison operation
            return i, el           # Return if found
    return None, None              # If nothing found, return None