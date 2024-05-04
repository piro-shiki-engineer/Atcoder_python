def my_answer():
    N = int(input())
    grid_A = [list(input()) for _ in range(N)]
    grid_B = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            A_i_j = grid_A[i][j]
            B_i_j = grid_B[i][j]

            if A_i_j != B_i_j:
                print('{} {}'.format(i+1, j+1))
                exit()


if __name__ == '__main__':
    my_answer()