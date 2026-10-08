def truth_table(n):
    if n == 0:
        return [()]
    result = []
    for i in range(2 ** n):
        bin_str = bin(i)[2:]
        while len(bin_str) < n:
            bin_str = "0" + bin_str
        row = []
        for char in bin_str:
            row.append(int(char))
        result.append(tuple(row))
    return result
