def my_answer():
    N = int(input())
    A_list = list(map(int, input().split()))

    total_without_n = sum(A_list)
    if total_without_n >= 0:
        print(-1*total_without_n)
    else:
        print(-1*total_without_n)


if __name__ == '__main__':
    my_answer()
