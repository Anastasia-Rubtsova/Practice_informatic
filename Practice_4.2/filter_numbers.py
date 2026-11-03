def filter_numbers(items):
    result = []
    for item in items:
        if isinstance(item, int) and not isinstance(item, bool):
            result.append(item)
    return result
