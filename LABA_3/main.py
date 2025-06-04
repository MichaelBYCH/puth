import time
from datetime import datetime


def log_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"[{start_datetime}] Функция '{func.__name__}' вызвана с аргументами: {args}\n")

        result = func(*args, **kwargs)

        end_time = time.time()
        end_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        execution_time = end_time - start_time

        with open("log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(
                f"[{end_datetime}] Функция '{func.__name__}' завершена. Время выполнения: {execution_time:.2f} сек.\n")

        return result

    return wrapper


@log_decorator
def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        raise ValueError("Неподдерживаемая операция")


if __name__ == "__main__":
    result = calculate(10, 5, '+')
    print(f"Результат: {result}")