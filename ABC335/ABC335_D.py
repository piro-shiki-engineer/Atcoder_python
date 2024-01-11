def my_answer():
    N = int(input())
    table = [[0 for _ in range(N)] for _ in range(N)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上
    part = 1
    step = 1

    center_point = (N//2, N//2)
    table[center_point[0]][center_point[1]] = 'T'
    x, y = center_point

    while part < N ** 2:
        for direction in directions:
            for _ in range(step):
                # 現在の方向に進む
                x += direction[0]
                y += direction[1]

                # グリッドの範囲内かどうか確認
                if 0 <= x < N and 0 <= y < N and table[x][y] == 0:
                    table[x][y] = part
                    part += 1
                    if part == N ** 2:  # 最後のパーツに到達した場合
                        break
            # 右または左に移動した後にステップ数を増やす
            if direction in [(0, 1), (0, -1)]:
                step += 1


    print(table)


if __name__ == '__main__':
    my_answer()
