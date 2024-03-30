def my_answer():
    N, A, B = map(int, input().split())
    D = list(map(int, input().split()))

    # ユニークなイベント日をセットで取得
    set_D = {d % (A + B) for d in D}

    # セットをリストに変換し、ソート
    D = list(set_D)
    D.sort()

    # リストの最後に週の周期を考慮した要素を追加
    D.append(D[0] + A + B)

    # 隣接するイベント間のギャップを確認
    ans = 'No'
    for i in range(len(D) - 1):
        if D[i + 1] - D[i] - 1 >= B:
            ans = 'Yes'
            break

    print(ans)

if __name__ == '__main__':
    my_answer()
