def my_answer():
    H, W, N = map(int, input().split())
    T = input()
    grid = []
    for _ in range(H):
        grid.append(list(input()))
    dw = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    dh = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
    count = 0
    possible_points = []
    # 着陸が陸地のみ候補に入れる
    for i in range(1, H-1):
        for j in range(1, W-1):
            if grid[i][j] == '.':
                possible_points.append([i, j])

    for possible_point in possible_points:
        now_x = possible_point[1]
        now_y = possible_point[0]
        # print("開始位置：{}行{}列".format(now_state_y, now_state_x))
        for act in T:
            if act == 'L':
                now_x -= 1
            elif act == 'R':
                now_x += 1

            if act == 'U':
                now_y -= 1
            elif act == 'D':
                now_y += 1

            # now_x += dw[act]
            # now_y += dh[act]
            # print(grid[now_state_y][now_state_x])
            if grid[now_y][now_x] == "#":
                break
        # print("終了位置：{}行{}列".format(now_state_y, now_state_x))
        if grid[now_y][now_x] == '.':
            count += 1

    print(count)


if __name__ == '__main__':
    my_answer()
