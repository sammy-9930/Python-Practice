"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
"""

def is_isogram(string):
    #your code here
    if string == "":
        return True 
    string = string.lower()
    is_isogram = {}
    for char in string:
        is_isogram[char] = is_isogram.get(char, 0) + 1 
    for key,value in is_isogram.items():
        if value > 1:
            return False 
    return True 

def is_isogram(string):
    #your code here
    seen = [False] * 26 
    string = string.lower()
    for letter in string:
        ind = ord(letter) - ord('a')
        if seen[ind]:
            return False 
        seen[ind] = True 
    return True