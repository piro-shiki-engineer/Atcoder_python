def my_answer():
    N, M, X = map(int, input().split())
    exp_each_text = []
    cost_each_text = []
    ans = 10**15

    for i in range(N):
        row = list(map(int, input().split()))
        cost_each_text.append(row[0])
        exp_each_text.append(row[1:])

    for i in range(1 << N):
        cost = 0
        level_each_algo = [0 for _ in range(M)]
        for shift in range(N):
            if (i >> shift) & 1 == 1:
                cost += cost_each_text[shift]
                for j in range(M):
                    level_each_algo[j] += exp_each_text[shift][j]
            if min(level_each_algo) >= X:
                ans = min(ans, cost)

    if ans == 10**15:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    my_answer()
