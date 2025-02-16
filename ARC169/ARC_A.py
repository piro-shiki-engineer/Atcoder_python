
def my_answer():
    N = int(input())
    A = list(map(int, input().split()))
    P = list(map(int, input().split()))
    count_zero = 0
    count_plus = 0
    count_minus = 0

    for j in range(2, N + 1):
        count_minus += A[j - 1]

    for i in range(4000):
        for j in range(2, N + 1):
            A[P[j - 2] - 1] += A[j - 1]
            count_minus += A[j - 1]

        if A[0] > 0:
            count_plus += 1
            count_zero = 0
            count_minus = 0
            if count_plus == N - 1:
                print("+")
                break

        elif A[0] < 0:
            count_plus = 0
            count_zero = 0
            if count_minus == N - 1:
                print("-")
                break
            count_minus = 0

        else:
            count_plus = 0
            count_zero += 1
            count_minus = 0
            if count_zero == 10:
                print(0)
                break

    # for i in range(4000):
    #     for j in range(2, N+1):
    #         A[P[j - 2] - 1] += A[j - 1]
    #     if A[0] > 0:
    #         count_plus += 1
    #         count_zero = 0
    #         count_minus = 0
    #         if count_plus == N-1:
    #             print("+")
    #             break
    #
    #     elif A[0] < 0:
    #         count_plus = 0
    #         count_zero = 0
    #         count_minus += 1
    #         if count_minus == N-1:
    #             print("-")
    #             break
    #
    #     else:
    #         count_plus = 0
    #         count_zero += 1
    #         count_minus = 0
    #         if count_zero == N-1:
    #             print(0)
    #             break
    #



if __name__ == '__main__':
    my_answer()