# Q1.2 check if a string is a permutation of another string
 
def checkPermutation(str1, str2):
    if ''.join(sorted(str1)) == ''.join(sorted(str2)):
        return True
    return False

def characterCounter(str):
    dic = dict()
    for s in str:
        if s not in dic:
            dic[s] = 1
        else:
            dic[s] += 1
    return dic

def checkPermutation2(str1, str2):
    if characterCounter(str1) == characterCounter(str2):
        return True
    return False
 
print checkPermutation("abcde", "dcbea")   
print checkPermutation("abcde", "dcbeac")
print checkPermutation2("abcde", "dcbea")   
print checkPermutation2("abcde", "dcbeac")   
   
    