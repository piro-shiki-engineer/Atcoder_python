def my_answer():
    n = int(input())
    beans = {}
    ans = -10**10

    for _ in range(n):
        delicious, color = map(int, input().split())
        if str(color) in (beans.keys()):
            beans[str(color)].append(delicious)
        else:
            beans[str(color)] = []
            beans[str(color)].append(delicious)

    for color in beans.keys():
        ans = max(ans, min(beans[color]))

    print(ans)


if __name__ == '__main__':
    my_answer()
