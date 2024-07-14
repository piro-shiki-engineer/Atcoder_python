import heapq
import sys


def dijkstra(N, adj_list, vertex_weights):
    inf = float("inf")
    dist = [inf] * N
    dist[0] = vertex_weights[0]
    pq = [(vertex_weights[0], 0)]  # (distance, vertex)

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, edge_weight in adj_list[u]:
            new_dist = current_dist + edge_weight + vertex_weights[v]

            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist


def main():
    N, M = map(int, input().split())
    node_weights = list(map(int, input().split()))
    adj_list = [[] for _ in range(N)]

    for _ in range(M):
        u, v, edge_weight = map(int, input().split())
        adj_list[u-1].append((v-1, edge_weight))
        adj_list[v-1].append((u-1, edge_weight))

    dist = dijkstra(N, adj_list, node_weights)

    results = []
    for i in range(1, N):
        if dist[i] == float("inf"):
            results.append("-1")
        else:
            results.append(str(dist[i]))

    print(" ".join(results))


if __name__ == "__main__":
    main()
