def insertion_sort(arr):
    res = list(arr)
    for i in range(1, len(res)):
        j = i
        while j > 0 and res[j - 1] > res[j]:
            res[j - 1], res[j] = res[j], res[j - 1]
            j -= 1
    return res
