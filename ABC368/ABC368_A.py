def main():
    N, K = map(int, input().split())
    cards = list(map(int, input().split()))

    for i in range(N-K, N):
        print(cards[i], end=' ')

    for j in range(N-K):
        print(cards[j], end=' ')


if __name__ == '__main__':
    main()
