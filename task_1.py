# Задача 1 - Пифагоровы штаны. Создайте функцию, которая будет принимать в себя массив несортированных чисел и вернёт
# boolean значение в зависимости от того, можно ли из заданных значений составить пифагоров треугольник с
# соответствующими длинами сторон.
# Тесты:
# [5, 3, 4] -> True
# [6, 8, 10] -> True
# [100, 3, 65] -> False

def function(array):
    array.sort()

    count = 0

    for element in array:
        array[count] = element ** 2
        count += 1

    return True if array[0] + array[1] == array[2] else False

print(function([5, 3, 4]))
print(function([6, 8, 10]))
print(function([100, 3, 65]))
