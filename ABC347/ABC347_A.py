def my_answer():
    N, K = map(int, input().split())
    A_list = list(map(int, input().split()))

    for A_i in A_list:
        if A_i % K == 0:
            print(A_i // K, end=' ')


if __name__ == '__main__':
    my_answer()
