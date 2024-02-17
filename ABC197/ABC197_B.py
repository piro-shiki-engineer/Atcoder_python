def my_answer():
    H, W, X, Y = map(int, input().split())
    X = X - 1
    Y = Y - 1
    grid = []

    for i in range(H):
        string = input()
        row = list(string)
        grid.append(row)

    up = 0
    down = 0
    left = 0
    right = 0

    # 要素の左（自身を含む）
    for left_i in range(Y+1):
        if grid[X][left_i] == '.':
            left += 1
        elif grid[X][left_i] == '#':
            left = 0
    # 要素の右（自身を除く）
    for right_i in range(W-1, Y, -1):
        if grid[X][right_i] == '.':
            right += 1
        elif grid[X][right_i] == '#':
            right = 0
    # 要素の上（自身を除く）
    for up_i in range(X):
        if grid[up_i][Y] == '.':
            up += 1
        elif grid[up_i][Y] == '#':
            up = 0
    # 要素の下（自身を除く）
    for down_i in range(H-1, X, -1):
        if grid[down_i][Y] == '.':
            down += 1
        elif grid[down_i][Y] == '#':
            down = 0

    # print(left, right, up, down)
    ans = up + down + left + right
    print(ans)


if __name__ == '__main__':
    my_answer()
