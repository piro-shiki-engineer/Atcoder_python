def main():
    N = int(input())
    A = list(map(int, input().split()))

    left_unique = [0] * (N + 1)
    left_set = set()
    for i in range(N):
        left_set.add(A[i])
        left_unique[i + 1] = len(left_set)

    right_unique = [0] * (N + 1)
    right_set = set()
    for i in range(N - 1, -1, -1):
        right_set.add(A[i])
        right_unique[i] = len(right_set)

    # 最後に和の最大
    max_unique_sum = 0
    for i in range(N + 1):
        max_unique_sum = max(max_unique_sum, left_unique[i] + right_unique[i])

    print(max_unique_sum)


if __name__ == "__main__":
    main()
