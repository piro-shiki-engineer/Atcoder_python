def my_answer():
    Q = int(input())
    A = []
    for i in range(Q):
        flag = True
        first, second = 0, 0
        first, second = map(int, input().split())
        print(first, second)
        if first == 1:
            if flag:
                A[0] = second
                flag = False
            else:
                if len(A) == 1:
                    A[0] = second
                else:
                    A[-1] = second
        elif first == 2:
            print(A[-second])


if __name__ == '__main__':
    my_answer()
