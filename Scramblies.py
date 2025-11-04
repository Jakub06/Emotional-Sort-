from collections import Counter
def scramble(s1,s2):

    if len(s1)<len(s2):
        return False
    
    count_s1 = Counter(s1)
    count_s2 = Counter(s2)
    
    for char, freq in count_s2.items():
        if count_s1[char] < freq:
            return False
    
    return True