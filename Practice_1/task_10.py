# задача 10

def index_of_min(values):
    if not values:
        return -1
    min_index = 0
    for i, num in enumerate(values):
        if num < values[min_index]:
            min_index = i
    return min_index

nums = input("Введите числа через пробел: ")
nums_array = list(map(int, nums.split()))
result = index_of_min(nums_array)
if result != -1:
    print("Минимальное число", nums_array[result], "с индексом", result)
else:
    print("Список пуст!")
