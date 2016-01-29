#Q1.1 determine whether a string has all unique characters

from itertools import permutations

# method 1 permutate through all possible pairs of characters
def isUnique(str):
    for i, j in permutations(range(len(str)),2):
        if str[i] == str[j]:
            return False
    return True
    
print isUnique("what the heck")

# method 2 use a dictionary
def isUnique2(str):
    mapping = dict()
    for s in str:
        if s not in mapping:
            mapping[s] = True
        else:
            return False
    return True
    
print isUnique2("Wha")