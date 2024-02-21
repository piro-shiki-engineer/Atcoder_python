def my_answer():
    N, K = map(int, input().split())
    vlg_per_friend = {}
    cash_per_friend = []
    A_i_before = 0
    for _ in range(N):
        A_i, B_i = map(int, input().split())
        if A_i in vlg_per_friend:
            vlg_per_friend[A_i] += B_i  # 既にキーがあれば加算
        else:
            vlg_per_friend[A_i] = B_i  # 新しいキーなら設定

    vlg_per_friend = sorted(vlg_per_friend.items(), key=lambda x: x[0])
    village_now = 0

    # print(vlg_per_friend)
    for i in range(len(vlg_per_friend)):
        village, can_get_cash = vlg_per_friend[i]

        if K >= (village - village_now):
            K -= (village - village_now)
            K += can_get_cash
            village_now = village
        else:
            break
    #残った金額による移動
    village_now += K
    print(village_now)


if __name__ == '__main__':
    my_answer()
