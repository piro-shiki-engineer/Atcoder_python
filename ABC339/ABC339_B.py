def my_answer():
    H, W, N = map(int, input().split())
    field = [['.' for j in range(W)] for i in range(H)]

    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 上、右、下、左、
    dir_index = 0  # 最初は上を向いている
    taka_j, taka_i = 0, 0

    for i in range(N):

        if field[taka_i][taka_j] == '.':
            field[taka_i][taka_j] = '#'
            dir_index = (dir_index + 1) % 4

        elif field[taka_i][taka_j] == '#':
            field[taka_i][taka_j] = '.'
            dir_index = (dir_index + 3) % 4 #マイナスは使わずに余りを元に行動選択

        next_pos = dirs[dir_index]
        if taka_j < 0: taka_j += W
        if taka_j >= W: taka_j -= W
        if taka_i < 0: taka_i += H
        if taka_i >= H: taka_i -= H

        taka_j = (taka_j + next_pos[0]) % H
        taka_i = (taka_i + next_pos[1]) % W

    for x in range(H):
        print(''.join(field[x]))

def my_answer2():
    H, W, N = map(int, input().split())
    field = [['.' for j in range(W)] for i in range(H)]

    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 上、右、下、左、
    dir_index = 0  # 最初は上を向いている

    taka_i, taka_j = 0, 0  # 高橋君の初期位置

    for _ in range(N):
        if field[taka_i][taka_j] == '.':  # 現在のマスが白の場合
            field[taka_i][taka_j] = '#'  # マスを黒に塗り替え
            dir_index = (dir_index + 1) % 4  # 時計回りに90度回転
        else:  # 現在のマスが黒の場合
            field[taka_i][taka_j] = '.'  # マスを白に塗り替え
            dir_index = (dir_index + 3) % 4  # 反時計回りに90度回転

        # 次のマスに進む
        taka_i = (taka_i + dirs[dir_index][0]) % H  # 行の更新
        taka_j = (taka_j + dirs[dir_index][1]) % W  # 列の更新

    for x in field:
        print(''.join(x))

def gpt_answer():
    h, w, n = map(int, input().split())  # グリッドの高さ、幅、操作回数を入力から取得
    ans = [['.' for _ in range(w)] for _ in range(h)]  # グリッドの初期化

    dx = [-1, 0, 1, 0]  # 上、右、下、左への移動を表すx方向の変化量
    dy = [0, 1, 0, -1]  # 上、右、下、左への移動を表すy方向の変化量

    x, y, m = 0, 0, 0  # 現在の位置(x, y)と向いている方向mの初期化

    for _ in range(n):
        if ans[x][y] == '.':  # 現在のマスが白の場合
            ans[x][y] = '#'  # マスを黒に塗り替え
            m += 1
        else:  # 現在のマスが黒の場合
            ans[x][y] = '.'  # マスを白に塗り替え
            m += 3
        m %= 4  # mが4以上にならないように調整

        x += dx[m]  # x座標を更新
        y += dy[m]  # y座標を更新

        # トーラス状のグリッドの端を超えた場合の処理
        if x < 0: x += h
        if x >= h: x -= h
        if y < 0: y += w
        if y >= w: y -= w

    # グリッドの状態を出力
    for row in ans:
        print(''.join(row))


if __name__ == '__main__':
    my_answer()
