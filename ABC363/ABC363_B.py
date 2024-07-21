def my_answer():
    N, T, P = map(int, input().split())
    hair_lengths = list(map(int, input().split()))
    diff_day = []
    ans = 0

    for i in range(N):
        diff_day.append(max(0, T - hair_lengths[i]))
    diff_day = sorted(diff_day)

    for i in range(P):
        ans = max(ans, diff_day[i])

    print(ans)


if __name__ == '__main__':
    my_answer()
