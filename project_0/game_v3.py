import numpy as np
from game_v1 import score_game

number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1
    lower_limit = 1
    upper_limit = 101
    predict = 50  # Начинаем угадывание с середины возможного диапазона
    while predict != number:  # Условие, при котором функция будет выполняться 
        # пока предположение не будет равным
        # загаданному числу
        if predict > number:
            upper_limit = predict
        else:
            lower_limit = predict
        count += 1  # Прибавляем единицу к счётчику каждый раз, когда цикл проходит круг
        predict = lower_limit + (upper_limit - lower_limit) // 2  # Присваиваем predict новое значение по формуле
        # бинарного поиска
    return count  # Выход из функции при нахождении нужного числа и вывод количества попыток


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
