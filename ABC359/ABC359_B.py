def my_answer():
    N = int(input())
    A = list(map(int, input().split()))
    person_index_by_color = {i: [] for i in range(1, N+1)}
    count = 0

    for index, A_i in enumerate(A):
        person_index_by_color[A_i].append(index)

    for place_i, place_j in person_index_by_color.values():
        if abs(place_i - place_j) == 2:
            count += 1
# O(N + M) →　N is length of A, M is number of colors
    print(count)


if __name__ == '__main__':
    my_answer()
