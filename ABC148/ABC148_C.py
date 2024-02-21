def my_answer():
    A, B = map(int, input().split())
    snacks = 0
    if A < B:
        tmp = A
        A = B
        B = tmp
    snacks = B
    while snacks % A != 0:
        snacks = snacks + B

    print(snacks)


if __name__ == '__main__':
    my_answer()
