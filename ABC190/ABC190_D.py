def my_answer():
    N = int(input())

    i = 1
    ans = 0

    while i**2 <= 2*N:
        # 2Nをiで割ったあまりが0つまり、整数
        if 2*N % i == 0:
            x = i
            y = 2*N // i
            if x % 2 != y % 2:
                ans += 2
        i += 1
    print(ans)


if __name__ == '__main__':
    my_answer()
