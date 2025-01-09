def overlap_lists(arr1, arr2):
    res = []
    for number in arr1:
        if number in arr2:
            res.append(number)
    return res 

l1 = [10, 15, 6, 9, 12, 8, 4]
l2 = [14, 6, 19, 4, 7, 10, 11]
print(overlap_lists(l1, l2))

