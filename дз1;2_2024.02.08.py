"""
1. Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните в переменные, а затем выведите на экран.
Используйте функции для консольного ввода input() и консольного вывода print().
Попробуйте также через встроенную функцию id() понаблюдать,
какие типы объектов могут изменяться и сохранять за собой адрес в оперативной памяти.
"""
a = 1
b = "string"
c = object()
print(id(c))

print(a)
print(b)
print(c)

print("Введите число")
d = input()
print("Значение из консольного ввода: " + d)
print("Введите строку")
e = input()
print("Значение из консольного ввода: " + e)
print(id(c))
print(id(a))
print(id(e))

"""
2. Пользователь вводит время в секундах.
Рассчитайте время и сохраните отдельно в каждую переменную количество часов, минут и секунд.
Переведите время в часы, минуты, секунды и сохраните в отдельных переменных.
Используйте приведение типов для перевода строк в числовые типы.
Предусмотрите проверку строки на наличие только числовых данных через встроенный строковый метод .isdigit().
"""

print("Введите секунды")
input = input()

if input.isdigit():
    seconds = int(input)
    print("seconds:" + str(seconds))
    minutes = seconds / 60
    print("minutes: " + str(minutes))
    hour = minutes / 60
    print("hour: " + str(hour))
else:
    print(input + " не число")

    """
    3. Запросите у пользователя через консоль число n (от 1 до 9). Найдите сумму чисел n + nn + nnn.

    Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

    Выведите данные в консоль.
    """
    print(" Введите число от 1 до 9")

    input_value = input()
    if not input_value.isdigit() or (int(input_value) < 1 or int(input_value) > 9):
        print("Число не подходит")
    else:
        first_int = int(input_value)
        second_int = first_int + first_int * 10
        third_int = second_int + first_int * 100
        print("Результат: ")
        print(first_int + second_int + third_int)

        """
        4. Реализуйте структуру данных «Участники спора». Она должна представлять собой
        список (list) словарей (dict).
        Каждый словарь хранит информацию об отдельном участнике. Словарь содержит
        пары «ключ-значение» параметрами, то есть характеристиками участника:
        наименование, статус, ИНН.
        Заполнение данных должно быть произведено пользователем через консоль для трёх
        различных участников.
        Выведите полученные данные в консоль.
        """


        def make_dictionary():
            print("Введите имя участника спора")
            name = input()
            print("Введите статус участника спора")
            status = input()
            print("Введите ИНН участника спора")
            inn = input()
            dictionary = dict()
            dictionary['name'] = name
            dictionary['status'] = status
            dictionary['inn'] = inn
            return dictionary


        result = list()
        result.append(make_dictionary())
        result.append(make_dictionary())
        result.append(make_dictionary())
        print(result)