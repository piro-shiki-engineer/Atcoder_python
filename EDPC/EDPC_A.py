def my_answer():
    N = int(input())
    height_per_floor = list(map(int, input().split()))
    dp = [10**15 for _ in range(N)]

    dp[0] = 0
    dp[1] = abs(height_per_floor[0] - height_per_floor[1])

    for i in range(2, N, 1):
        cost1 = dp[i-1] + abs(height_per_floor[i-1] - height_per_floor[i])
        cost2 = dp[i-2] + abs(height_per_floor[i-2] - height_per_floor[i])
        dp[i] = min(cost1, cost2)

    print(dp[N-1])


if __name__ == '__main__':
    my_answer()
