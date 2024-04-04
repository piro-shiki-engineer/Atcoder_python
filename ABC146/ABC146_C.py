def my_answer():
    A, B , X = map(int, input().split())

    if (A * 1 + B * 1) > X:
        print(0)
        exit()

    min_N = 1
    max_N = 10 ** 10

    while max_N - min_N > 1:
        median = (min_N + max_N) // 2
        if (A * median + B * len(str(median))) <= X:
            min_N = median
        else:
            max_N = median

    if min_N > 10 ** 9:
        min_N = 10 ** 9

    print(min_N)


if __name__ == '__main__':
    my_answer()

