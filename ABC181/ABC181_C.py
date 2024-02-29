def my_answer():
    N = int(input())
    coordinates = [tuple(map(int, input().split())) for _ in range(N)]
    x_1, y_1 = coordinates[0][0], coordinates[0][0]
    left_side = 0
    right_side = 0
    count = 0

    for x_1, y_1 in coordinates:
        for x_2, y_2 in coordinates:
            for x_3, y_3 in coordinates:
                if (x_1 == x_2 and y_1 == y_2) or (x_2 == x_3 and y_2 == y_3) or (x_3 == x_1 and y_3 == y_1):
                    continue
                left_side = (y_3 - y_1) * (x_2 - x_1)
                right_side = (y_2 - y_1) * (x_3 - x_1)
                if left_side == right_side:
                    print('Yes')
                    exit()
    print('No')


if __name__ == '__main__':
    my_answer()
