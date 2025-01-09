"""Concatenate integers into a single number."""
def combine_numbers(arr):
    res = ""
    for number in arr:
        res += str(number)
    return str(res)


l1 = [int(x) for x in input("Enter numbers, separated by space: ").split()]
print(combine_numbers(l1))