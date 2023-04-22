"""Игры угадай число.
   Компьютер сам загадывает и угадывает число.
"""

import numpy as np


def random_predict(number:int = 1) -> int:
    """Рандомно угадывает число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    start = 1 # Начало диапазона, в котором компьютер отгадывает число
    end = 101 # Конец диапазона, в котором компьютер отгадывает число

    while True:
        count += 1
        predict_number = np.random.randint(start, end) #Предполагаемое число

        if predict_number > number:
            end = predict_number
        elif predict_number < number:
            start = predict_number + 1
        else:
            break #Выход из цикла, если число угадано

    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 попвток угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # Список для сохранения количество попыток
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = 1000) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # Находим среднее количество попыток

    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


#RUN
if __name__ == '__main__':
    score_game(random_predict)