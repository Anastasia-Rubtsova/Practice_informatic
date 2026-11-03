def filter_numbers(items):
    result = []
    for item in items:
        # isinstance(True, int) == True, поэтому нужно исключить bool
        if isinstance(item, int) and not isinstance(item, bool):
            result.append(item)
    return result
