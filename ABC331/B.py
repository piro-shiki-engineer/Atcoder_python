def my_answer():
    N, price_6, price_8, price_12 = map(int, input().split())
    answer = 100000000

    for i in range(101):
        for j in range(101):
            for k in range(101):
                if 6*i + 8*j + 12*k >= N:
                    answer = min(answer, price_6*i+price_8*j+price_12*k)

    print(answer)


if __name__ == '__main__':
    my_answer()
