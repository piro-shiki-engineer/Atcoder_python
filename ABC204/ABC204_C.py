from collections import deque

def get_possibles_sities_num(n: int, start: int, edges: dict):
    que = deque()
    count = 0
    already_visited = [False for _ in range(n)]
    que.append(start)
    already_visited[start] = True
    count += 1

    while len(que) > 0:
        now_city = que.popleft()
        for to_city in edges[now_city]:
            if not already_visited[to_city]:
                que.append(to_city)
                already_visited[to_city] = True
                count += 1
    return count


def my_answer():
    N, M = map(int, input().split())
    edges = {i: [] for i in range(N)}
    for _ in range(M):
        A, B = map(int, input().split())
        edges[A-1].append(B-1)
    ans = 0
    for i in range(N):
        ans += get_possibles_sities_num(N, i, edges)

    print(ans)


if __name__ == '__main__':
    my_answer()
