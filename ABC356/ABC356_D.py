def my_answer():
    N, M = map(int, input().split())
    mod = 998244353
    ans = 0
    M_binary = bin(M)
    for k in range(N):
        k_binary = bin(k)
        result_and = int(str(k_binary) & str(M_binary), 2)
        ans += result_and % mod

    print(ans)


if __name__ == '__main__':
    my_answer()
