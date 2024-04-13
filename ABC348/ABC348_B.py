def my_answer():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    point_from_apoint = [[None]*n for i in range(n)]
    distance = 0

    for i in range(len(points)):
        for j in range(len(points)):
            point_from_apoint[i][j] = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2

    for index, distance_from_i_to_j in enumerate(point_from_apoint):
        print(distance_from_i_to_j.index(max(distance_from_i_to_j))+1)


if __name__ == '__main__':
    my_answer()
