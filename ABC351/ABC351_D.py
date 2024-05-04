def my_answer():
    H, W = map(int, input().split())
    grid = [list(input())for i in range(H)]
    init_points = []
    can_move = True
    # 上、下、左、右
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(H):
        for j in range(W):
            for dir in range(4):
                if j+dy[dir] == -1 or i+dx[dir] == -1:
                    pass
                else:
                    if grid[j+dy[dir]][i+dx[dir] == '.':
                        init_points.append([i, j])



if __name__ == '__main__':
    my_answer()