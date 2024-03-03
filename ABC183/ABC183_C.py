import itertools

def my_answer():
    N, K = map(int, input().split())
    time_list = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for root in itertools.permutations(range(1, N)):
        now_time = 0
        now_time += time_list[0][root[0]]
        now_city = root[0]

        for i in range(1, N-1):
            to_city = root[i]
            now_time += time_list[now_city][to_city]
            now_city = to_city

        now_time += time_list[now_city][0]

        if now_time == K:
            ans += 1

    print(ans)


if __name__ == '__main__':
    my_answer()
