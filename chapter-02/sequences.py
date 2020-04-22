# An empty list
list() 

list1 = [1, 2, 3, 4]
list1.append(1)
print ("Print list1:", list1)
list2 = list1 * 2
print ("Print list1:", list1)

# Functions
print("Minimum in list1 is ", min(list1))
print("Maximum in list1 is", max(list1))

# Insert an value 2 at index 0
list1.insert(0, 2)
print("Updated list1 is ", list1)

# Reversing
list1.reverse()
print("Revised list 1 is ", list1)

# Extending
list2 = [11, 12]
list1.extend(list2)
print("Updated list 1 is",list1)

# Functions
print("Sum of all the elements in list1 is", sum(list1))
print("length of list 1 is ", len(list1))

# Sorting
list1.sort()
print("Sorted list 1 is", list1)

# remove value 12 form the list
list1.remove(12)
print("list 1 after removal of element 12 is ", list1)

