def my_answer():
    N = int(input())
    A_list = list(map(int, input().split()))

    for i in range(N-1):
        print(A_list[i]*A_list[i+1], end=' ')


if __name__ == '__main__':
    my_answer()
