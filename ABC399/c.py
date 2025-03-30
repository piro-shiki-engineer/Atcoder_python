def count_connected_components_iterative(adj_list, n):
    visited = [False] * n
    count = 0

    for start in range(n):
        if visited[start]:
            continue

        count += 1
        stack = [start]
        visited[start] = True

        while stack:
            node = stack.pop()

            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

    return count


def main():
    N, M = map(int, input().split())

    adj_list = [[] for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        adj_list[u - 1].append(v - 1)
        adj_list[v - 1].append(u - 1)

    connected_components = count_connected_components_iterative(adj_list, N)
    min_edges_to_remove = M - N + connected_components

    print(max(min_edges_to_remove, 0))


if __name__ == "__main__":
    main()
