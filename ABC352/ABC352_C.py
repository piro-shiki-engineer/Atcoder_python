def my_answer():
    N = int(input())
    giants = []
    for _ in range(N):
        A_i, B_i = map(int, input().split())
        giants.append((A_i, B_i))

    # A_i + B_iが大きい順にソート
    giants.sort(key=lambda x: (x[0] + x[1]), reverse=True)

    max_height = 0
    current_height = 0
    for A, B in giants:
        current_height += A
        max_height = max(max_height, current_height + B - A)

    print(max_height)


if __name__ == '__main__':
    my_answer()
