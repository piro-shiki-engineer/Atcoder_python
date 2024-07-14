def my_answer():
    N = int(input())
    pairs = [list(map(int, input().split())) for _ in range(N)]
    ans = [0] * N

    min_total, max_total = 0, 0
    for L, R in pairs:
        min_total += L
        max_total += R

    if min_total > 0 or max_total < 0:
        print("No")
        return

    target = -min_total
    for i in range(N):
        L, R = pairs[i]
        ans[i] = L
        diff = min(R - L, target)
        ans[i] += diff
        target -= diff

    if sum(ans) == 0:
        print("Yes")
        print(" ".join(map(str, ans)))
    else:
        print("No")


if __name__ == '__main__':
    my_answer()
