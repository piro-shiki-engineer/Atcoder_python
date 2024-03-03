def my_answer():
    N = int(input())
    A_list = list(map(int, input().split()))
    A_j_total = sum(A_list)
    total = 0

    for i in range(N-1):
        A_i = int(A_list[i])
        A_j_total -= A_i
        product = A_i * A_j_total
        total += product

    print(total % (10**9 + 7))


if __name__ == '__main__':
    my_answer()
