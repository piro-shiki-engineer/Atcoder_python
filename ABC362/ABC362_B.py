def my_answer():
    coordinates = [list(map(int, input().split())) for i in range(3)]

    for i in range(3):
        base_point = coordinates[i]
        point_1 = coordinates[(i + 1) % 3]
        point_2 = coordinates[(i + 2) % 3]

        vector_1 = [point_1[0] - base_point[0], point_1[1] - base_point[1]]
        vector_2 = [point_2[0] - base_point[0], point_2[1] - base_point[1]]

        if vector_1[0] * vector_2[0] + vector_1[1] * vector_2[1] == 0:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    my_answer()
