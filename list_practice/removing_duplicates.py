"""Checking and removing if there is any duplicate in the list.
Delete element from list if duplicate is found."""

def check_duplicate(l1):
    i = 0
    while i < len(l1):
        if l1[i] in l1[:i]:  # Check if the element already exists in the previous part of the list
            l1.pop(i) 
        else:
            i += 1  # Move to the next element only if no duplicate is found
    return l1


l1 = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print(check_duplicate(l1))
