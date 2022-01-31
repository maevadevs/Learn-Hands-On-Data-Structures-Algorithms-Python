def mergesort(lst):
    """Implementation of the mergesort algorithm. 
    Sort a list by dividing and breaking the original list down to single elements and recursively putting them back together.
    The `merge_and_sort()` function takes care of merging back the sorted sublists together."""
    
    #print('splitting', lst)
    
    n = len(lst)
    
    # Base case for recurrence: 1 element in the array, return
    if n == 1:
        return lst
    
    # Else, Split the arr into 2
    mid_i = n // 2
    left = lst[:mid_i]
    right = lst[mid_i:]
    
    # Recurrence until reaching base case
    left = mergesort(left)
    right = mergesort(right)
    
    # If reached here, then the sublists have been broken down. 
    # Merge back while sorting and return the sorted list.
    sorted_lst = merge_and_sort(left, right, lst)
    return sorted_lst


def merge_and_sort(left, right, lst):
    """Merge two lists together while comparing and placing the elements from the two lists in the right order."""

    # Index references for left, right, and lst
    i = 0
    j = 0
    k = 0

    # Length of the sublists
    len_left = len(left)
    len_right = len(right)

    # Compare and merge
    while i < len_left and j < len_right:
        if left[i] < right[j]:
            lst[k] = left[i]
            i += 1
            k += 1
        else:
            lst[k] = right[j]
            j += 1
            k += 1

    # Append remnants from left if any
    while i < len_left:
        lst[k] = left[i]
        i += 1
        k += 1

    # Append remnants from right if any
    while j < len_right:
        lst[k] = right[j]
        j += 1
        k += 1

    #print('...merging', left, 'and', right,'=>', lst) 
    return lst