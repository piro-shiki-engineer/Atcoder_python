def my_answer():
    N, X, Y, Z = map(int, input().split())

    if X > Y:
        if Y < Z and Z < X:
            print('Yes')
        else:
            print("No")

    else: # X < Y
        if Y > Z and Z > X:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    my_answer()