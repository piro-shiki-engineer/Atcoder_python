def my_answer():
    H, W = map(int, input().split())
    s_i, s_j = map(int, input().split())
    s_i -= 1
    s_j -= 1
    grid = [list(input()) for _ in range(H)]
    X = input()

    for i in range(len(X)):
        if X[i] == 'L':
            if s_j > 0 and grid[s_i][s_j - 1] == '.':
                s_j -= 1
        elif X[i] == 'R':
            if s_j < W - 1 and grid[s_i][s_j + 1] == '.':
                s_j += 1
        elif X[i] == 'U':
            if s_i > 0 and grid[s_i - 1][s_j] == '.':
                s_i -= 1
        elif X[i] == 'D':
            if s_i < H - 1 and grid[s_i + 1][s_j] == '.':
                s_i += 1

    print(s_i + 1, s_j + 1)


if __name__ == '__main__':
    my_answer()
