import os
import numpy as np
from functions import read_data, calculate_statistics, calculate_derivative, calculate_integral, write_results

# Путь к директории с данными
data_dir = 'data'

# Получаем значения x
x_file = os.path.join(data_dir, 'xc.dat')
x_values = read_data(x_file)

# Получаем список всех файлов yc
y_files = []
for file in os.listdir(data_dir):
    if file.startswith('yc-') and file.endswith('.dat'):
        y_files.append(file)

# Обрабатываем каждый файл y
for y_file in y_files:
# Читаем значения y
    y_path = os.path.join(data_dir, y_file)
    y_values = read_data(y_path)

# Вычисляем статистические показатели
    stats = calculate_statistics(y_values)

# Вычисляем производную
    derivative = calculate_derivative(x_values, y_values)

# Вычисляем интеграл
    integral = calculate_integral(x_values, y_values)

# Записываем результаты в выходной файл
    output_file = f"out_{y_file}"
    write_results(output_file, y_file, stats, derivative, integral)

    print(f"Обработан файл {y_file}, результаты сохранены в {output_file}")

print("Все файлы успешно обработаны.")