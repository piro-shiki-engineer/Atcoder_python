def my_answer():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(N):
        if A[i] <= L:
            print(L, end=' ')
        elif L <= A[i] and A[i] <= R:
            print(A[i], end=' ')
        else:
            print(R, end=' ')


if __name__ == '__main__':
    my_answer()
