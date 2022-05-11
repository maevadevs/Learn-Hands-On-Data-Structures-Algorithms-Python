def linear_search(ls, search_el):
    for i, el in enumerate(ls):    # Loop through every single element
        if el == search_el:        # Compare with search element: The key comparison operation
            return i, el           # Return if found
    return None, None              # If nothing found, return None