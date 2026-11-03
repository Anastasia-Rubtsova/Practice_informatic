def count_duplicates(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    result = 0
    for char in counts:
        if counts[char] > 1:
            result += 1
    return result
