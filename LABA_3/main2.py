import time


def cache_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        # Create a key based on both positional and keyword arguments
        cache_key = str(args) + str(sorted(kwargs.items()))

        if cache_key in cache:
            print(f"Результат для {func.__name__}{args} взят из кэша")
            return cache[cache_key]

        # Calculate the result and save it in the cache
        result = func(*args, **kwargs)
        cache[cache_key] = result
        print(f"Результат для {func.__name__}{args} вычислен и сохранен в кэш")
        return result

    return wrapper


@cache_decorator
def fibonacci(n):
    print(f"Вычисляем fibonacci({n})...")
    time.sleep(0.1)  # Имитация сложных вычислений
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Результат fibonacci(10): {fibonacci(10)}")
    print(f"Время выполнения: {time.time() - start_time:.2f} сек.")

    print("\nВызываем повторно:")
    start_time = time.time()
    print(f"Результат fibonacci(10): {fibonacci(10)}")
    print(f"Время выполнения: {time.time() - start_time:.2f} сек.")