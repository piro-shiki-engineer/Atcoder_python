def my_answer():
    n = int(input())
    for i in range(1, n+1):
        if i % 3 == 0:
            print("x", end='')
        else:
            print("o", end='')


if __name__ == '__main__':
    my_answer()
