# Каждый элемент массива атакует элемент другого массива с тем же индексом массива.
# Выживший - это число с наибольшим значением.
# Если значение одинаковое, они оба погибают.
# Если одно из значений отсутствует (различная длина массивов), солдат с непустым значением выживает.
# Чтобы выжить, обороняющаяся сторона должна иметь больше выживших, чем атакующая сторона.
# В случае, если с обеих сторон одинаковое количество выживших, побеждает команда с наибольшей начальной силой атаки.
# Если общая сила атаки обеих сторон одинакова, верните True.
# Начальная сила атаки представляет собой сумму всех значений в каждом массиве.
# Тесты:
# zombies=[ 1, 3, 5, 7 ]   plants=[ 2, 4, 6, 8 ]  -> True
# zombies=[ 1, 3, 5, 7 ]   plants=[ 2, 4 ]  -> False
# zombies=[ 1, 3, 5, 7 ]   plants=[ 2, 4, 0, 8 ]  -> True
# zombies=[ 2, 1, 1, 1 ]   plants=[ 1, 2, 1, 1 ]  -> True
zombies = [ 2, 1, 1, 1 ]
plants = [ 1, 2, 1, 1 ]

def zombies_vs_plants(zombies, plants):
    # Функция, для подсчета суммы всех значений в указанном массиве.
    def sum_values(array):
        total_sum = 0
        for element in array:
            total_sum += element
        return total_sum

    # Начальная сила атаки каждого массива

    total_sum_zombies = sum_values(zombies)
    total_sum_plants = sum_values(plants)

    # Уравниваем длину массивов при возможных расхождениях

    while len(plants) < len(zombies):
        plants.append(0)

    while len(zombies) < len(plants):
        zombies.append(0)

    # Обходим массивы и проверяем какое значение больше. Меньшее значение превращаем в 0.

    count = 0

    for element_zombies in zombies:

        element_plants = plants[count]

        if element_zombies > element_plants:
            zombies[count] = element_zombies
            plants[count] = 0

        elif element_zombies < element_plants:
            plants[count] = element_plants
            zombies[count] = 0

        elif element_zombies == element_plants:
            zombies[count] = 0
            plants[count] = 0

        count += 1

    # создаем функцию, которая обходит измененные массивы и возвращает количество значений больше 0 (выживших)

    def survivors(array):
        count = 0
        for element in array:
            if element > 0:
                count += 1
        return count

    # Записываем результаты в переменные

    survivors_zombies = survivors(zombies)
    survivors_plants = survivors(plants)

    # проверяем условия

    if survivors_zombies < survivors_plants:
        return True
    elif survivors_zombies > survivors_plants:
        return False
    elif survivors_zombies == survivors_plants:
        if total_sum_plants > total_sum_zombies:
            return True
        elif total_sum_zombies > total_sum_plants:
            return False
        else:
            return True
# Выводим результат
print(zombies_vs_plants(zombies, plants))


