def truth_table(n):
    if n == 0:
        return [()]
    result = []
    for i in range(2 ** n):
        bin_str = bin(i)[2:]
        while len(bin_str) < n:
            bin_str = "0" + bin_str
        row = tuple(int(char) for char in bin_str)
        result.append(row)
    return result

def are_equivalent(f, g, n):
    table = truth_table(n)
    for row in table:
        if f(*row) != g(*row):
            return False
    return True
