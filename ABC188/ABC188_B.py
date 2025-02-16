def my_answer():
    N = int(input())
    A_vector = list(map(int, input().split()))
    B_vector = list(map(int, input().split()))
    Dot_val = 0

    for i in range(N):
        Dot_val += A_vector[i]*B_vector[i]

    if Dot_val == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    my_answer()
