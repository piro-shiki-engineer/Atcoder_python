def main():

    N, M = map(int, input().split())

    X = 0
    for i in range(M+1):
        X += N ** i
        if X <= 10 ** 9:
            continue
        else:
            print("inf")
            exit()
    print(X)

if __name__ == '__main__':
    main()
