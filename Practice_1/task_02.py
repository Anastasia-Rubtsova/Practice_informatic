# задача 2
def bytes_to_kilobytes(value):
    return value / 1024

def kilobytes_to_bytes(value):
    return value * 1024

print("Выберите преобразование:")
print("1: Байты в килобайты")
print("2: Килобайты в байты")
choice = input("Введите 1 или 2: ")

if choice == "1":
    bytes_value = float(input("Введите байты: "))
    k_bytes_value = bytes_to_kilobytes(bytes_value)
    print(f"Байты переведенные в килобайты: {k_bytes_value}")

elif choice == "2":
    k_bytes_value = float(input("Введите килобайты: "))
    bytes_value = kilobytes_to_bytes(k_bytes_value)
    print(f"Килобайты переведенные в байты: {bytes_value}")

else:
    print("Неверный выбор!")
