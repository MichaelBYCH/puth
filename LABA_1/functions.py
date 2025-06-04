import numpy as np
import os


def read_data(filename, method='numpy'):
    """
    Чтение данных из файла с помощью open() или np.loadtxt()

    Аргументы:
        filename (str): Путь к файлу
        method (str): Метод для чтения ('open' или 'numpy'), по умолчанию 'numpy'

    Возвращает:
        list или np.array: Данные из файла
    """
    if method == 'open':
        with open(filename, 'r') as f:
            data = [float(line.strip()) for line in f if line.strip()]
        return data
    else:  # По умолчанию numpy
        return np.loadtxt(filename)


def calculate_statistics(y):
    """
    Расчет статистических показателей для функции y = f(x)

    Аргументы:
        y (list или np.array): Значения функции

    Возвращает:
        dict: Словарь, содержащий статистические показатели (среднее, максимум, минимум)
    """
    if not isinstance(y, np.ndarray):
        y = np.array(y)

    stats = {
        'mean': np.mean(y),
        'max': np.max(y),
        'min': np.min(y)
    }

    return stats


def calculate_derivative(x, y):
    """
    Расчет производной для y = f(x) с использованием numpy.gradient

    Аргументы:
        x (list или np.array): значения x
        y (list или np.array): значения y функции y = f(x)

    Возвращает:
        np.array: Значения производной
    """
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    if not isinstance(y, np.ndarray):
        y = np.array(y)

    return np.gradient(y, x)


def calculate_integral(x, y):
    """
    Расчет определенного интеграла для y = f(x) методом прямоугольников

    Аргументы:
        x (list или np.array): значения x
        y (list или np.array): значения y функции y = f(x)

    Возвращает:
        float: Значение определенного интеграла
    """
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    if not isinstance(y, np.ndarray):
        y = np.array(y)

    # Метод прямоугольников: sum(y_i * Δx_i)
    dx = np.diff(x)
    y_mid = (y[:-1] + y[1:]) / 2  # Используем среднее соседних точек

    return np.sum(y_mid * dx)


def write_results(filename, input_filename, stats, derivative, integral):
    """
    Запись результатов расчетов в файл

    Аргументы:
        filename (str): Имя выходного файла
        input_filename (str): Имя исходного файла с данными
        stats (dict): Словарь со статистическими показателями
        derivative (list или np.array): Значения производной
        integral (float): Значение интеграла
    """
    with open(filename, 'w') as f:
        f.write(f"Исходный файл: {input_filename}\n\n")

        f.write("Статистические показатели:\n")
        f.write(f"Среднее: {stats['mean']}\n")
        f.write(f"Максимум: {stats['max']}\n")
        f.write(f"Минимум: {stats['min']}\n\n")

        f.write("Значения производной:\n")
        for val in derivative:
            f.write(f"{val}\n")
        f.write("\n")

        f.write(f"Определенный интеграл: {integral}\n")