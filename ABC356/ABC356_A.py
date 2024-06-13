def my_answer():
    N, L, R = map(int, input().split())

    for i in range(1, L):
        print(i, end=' ')

    for j in range(R, L-1, -1):
        print(j, end=' ')

    for k in range(R+1, N+1):
        print(k, end=' ')


if __name__ == '__main__':
    my_answer()
