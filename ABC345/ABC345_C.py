def my_answer():
    S = list(input())
    N = len(S)
    ans = 0

    # アルファベットをキーに持つ、数え上げ用の辞書型
    alphabet_count = {chr((ord('a')+i)): 0 for i in range(26)}
    # print(alphabet_count)

    for i in range(N):
        # 現在の文字までにいくつ同じ文字
        ans += i - alphabet_count[S[i]]
        alphabet_count[S[i]] += 1

    for alphabet_num in alphabet_count.values():
        if alphabet_num > 1:
            ans += 1
            break

    print(ans)


if __name__ == '__main__':
    my_answer()
