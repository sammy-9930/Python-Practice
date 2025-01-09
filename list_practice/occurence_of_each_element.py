# def occurence_of_each_element(arr1):
#     count = {}
#     for element in arr1:
#         count[element] = 1 + count.get(element, 0)
#     return count

def occurence_of_each_element(arr1):
    result = []
    for element in arr1:
        if element not in result:
            result.append(element)
            count = arr1.count(element)
            result.append(count)
    return result


l1 = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'E', 'B', 'D', 'B', 'E']
print(occurence_of_each_element(l1))

