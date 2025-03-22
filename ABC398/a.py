def main():
    N = int(input())
    res = ''

    if N % 2 == 0:
        for i in range(N//2-1):
            res += '-'
        res += ('==' + res)

    else:
        for i in range(N // 2):
            res += '-'
        res += ('=' + res)

    print(res)


if __name__ == '__main__':
    main()