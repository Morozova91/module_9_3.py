# "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# print(first)
# print(second)

# 1. В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков
# first и second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.

first_result = [(len(x) - len(y)) for x, y in zip(first, second) if len(x) != len(y)]
print(first_result)

# 2. В переменную second_result запишите генераторную сборку,
# которая содержит результаты сравнения строк в одинаковых позициях из списков first и second.
# Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.
second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]
print(second_result)





