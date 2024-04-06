def my_answer():
    N, K = map(int, input().split())
    teleport_each_city = list(map(int, input().split()))

    now_city = 1
    visited = [0]*N
    visited[now_city-1] = 1
    loop = []
    rest_step = K

    for _ in range(K):
        now_city = teleport_each_city[now_city - 1]
        visited[now_city-1] += 1
        rest_step -= 1

        if visited[now_city-1] == 2:
            loop.append(now_city)
        elif visited[now_city-1] == 3:
            break

    if rest_step == 0:
        pass
    else:
        for _ in range(rest_step % len(loop)):
            now_city = teleport_each_city[now_city-1]
    print(now_city)


if __name__ == '__main__':
    my_answer()
