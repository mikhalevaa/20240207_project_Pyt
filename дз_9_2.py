# массив
full_array = list(range(10, 25 * 10 ** 7, 3))

# функция
my_array = [x for x in range(10, 250000001, 25000000)]
print("Результат работы функции, 10 случайных чисел:", my_array)

# линейный поиск
print("Ввод данных для линейного поиска (по окончании ввода нажми Entr)")
target_element = int(input())
def linear_search(arr, target_element):
    for i in range(len(arr)):
        if arr[i] == target_element:
            return i
    return -1
result = linear_search(full_array, target_element)
if linear_search(full_array, target_element) != -1:
    print(f"Элемент {target_element} найден на позиции {result}, \
линейный поиск.")
else:
    print(f"Элемент {target_element} не найден в списке, линейный поиск.")
    
# бинарный поиск
print("Ввод данных для бинарного поиска (по окончании ввода нажми Entr)")
target_element = int(input())
def binary_search(arr, target_element):
    for i in range(len(arr)):
        if arr[i] == target_element:
            return i
    return -1
result = binary_search(full_array, target_element)
if result != -1:
    print(f"Элемент {target_element} найден на позиции {result}, \
бинарный поиск.")
else:
    print(f"Элемент {target_element} не найден в списке, бинарный поиск.")

# проверка


