def my_answer():
    N = int(input())
    adjacency_matrix = [list(map(int, input().split())) for _ in range(N)]

    for adjacency_row in adjacency_matrix:
        for i, node_val in enumerate(adjacency_row):
            if node_val == 1:
                print(i+1, end=' ')
        print()


if __name__ == '__main__':
    my_answer()
