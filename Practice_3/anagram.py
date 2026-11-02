def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    counts = [0] * 26
    for char in s1:
        counts[ord(char) - ord('a')] += 1
    for char in s2:
        counts[ord(char) - ord('a')] -= 1
        
    for count in counts:
        if count != 0:
            return False
    return True
