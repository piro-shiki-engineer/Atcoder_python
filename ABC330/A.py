def my_answer():
    N, L = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0

    for i in range(N):
        if A[i] >= L:
            count += 1

    print(count)


if __name__ == '__main__':
    my_answer()
