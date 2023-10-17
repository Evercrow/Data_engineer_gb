def fib_gen() -> int:
    """
    Бесконечный генератор чисел Фибоначчи
    :return: 
    """
    next_num = 0
    prev_num = 1
    while True:
        yield next_num
        next_num += prev_num
        prev_num = next_num


if __name__ == "__main__":
    f = fib_gen()
    for i in range(10):
        next(f)
    for i in range(10, 61):
        print(f"{i}:{next(f)}")
