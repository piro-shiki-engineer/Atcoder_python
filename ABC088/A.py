
def my_answer():
    N = int(input())
    a = list(map(int, input().split()))

    # 降順にソートする
    a.sort(reverse=True)
    score_a = 0
    score_b = 0

    for i in range(N):
        if i % 2 == 0:
            score_a += a[i]
        else:
            score_b += a[i]
    print(score_a - score_b)


if __name__ == '__main__':
    my_answer()
