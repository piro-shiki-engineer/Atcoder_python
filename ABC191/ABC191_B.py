def my_answer():
    N, X = map(int, input().split())
    A_list = list(map(int, input().split()))
    count_val = 0

    for i in range(N):
        val = A_list[i]
        if val != X:
            print(val, end=' ')
            count_val += 1
    if count_val == 0:
        print()


if __name__ == '__main__':
    my_answer()
