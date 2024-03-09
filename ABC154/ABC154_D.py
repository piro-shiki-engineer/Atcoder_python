def my_answer():
    N, K = map(int, input().split())
    possibles = list(map(int, input().split()))
    expected_values = [(possibles[i]+1)/2 for i in range(N)]

    ex_p_totals = [expected_values[0]]
    for i in range(1, N):
        ex_p_totals.append(ex_p_totals[i-1] + expected_values[i])

    ans = 0
    for i in range(N-K+1):
        if i == 0:
            tmp = ex_p_totals[i+K-1]
        else:
            # その前の文を除く　
            tmp = ex_p_totals[i+K-1] - ex_p_totals[i-1]
        ans = max(ans, tmp)
    print(ans)


if __name__ == '__main__':
    my_answer()
