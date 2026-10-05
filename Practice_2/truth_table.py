def truth_table(n):
    if n == 0:
        return [()]
    
    result = []
    for i in range(2 ** n):
        binary = format(i, f'0{n}b')
        row = tuple(int(bit) for bit in binary)
        result.append(row)
    return result


n = int(input("Введите количество переменных: "))
table = truth_table(n)

for row in table:
    print(row)
