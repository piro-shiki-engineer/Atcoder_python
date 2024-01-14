def my_answer():
    n = int(input())
    binary_n = []
    answer = 0

    while n != 0:
        binary_n.append(n % 2)
        n = n // 2

    for num in binary_n:
        if num == 0:
            answer += 1
        elif num == 1:
            break

    print(answer)


if __name__ == '__main__':
    my_answer()
