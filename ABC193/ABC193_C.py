import math


def my_answer():
    N = int(input())
    numbers = []
    num = 0
    a = 2
    b = 2
    flag = True
    while flag:
        num = a**b
        if num <= N:
            numbers.append(num)
            b += 1
        else:
            a += 1
            b = 2
            if a > math.sqrt(N):
                flag = False

    numbers = set(numbers)
    print(N - len(numbers))


if __name__ == '__main__':
    my_answer()
