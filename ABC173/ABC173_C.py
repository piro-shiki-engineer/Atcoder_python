def my_answer():
    H, W, K = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    ans = 0

    # 行を何行か、列を何行を赤い行とするかの決定
    for red_row in range(1 << H):
        for red_column in range(1 << W):
            black = 0
            # 各列が黒であるかを一マスずつ確認する
            for i in range(H):
                for j in range(W):
                    if red_row >> i & 1 == 0 and red_column >> j & 1 == 0:
                        if grid[i][j] == "#":
                            black += 1
            if black == K:
                ans += 1

    print(ans)


if __name__ == '__main__':
    my_answer()
