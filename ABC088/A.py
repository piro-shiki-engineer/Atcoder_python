
def my_answer():
    N = int(input())
    a = list(map(int, input().split()))

    # 降順にソートする
    a.sort(reverse=True)
    a_dict = {key: a[key] for key in range(N)}
    score_a = 0
    score_b = 0

    for key, value in a_dict.items():
        if key % 2 == 0 or key == 0:
            score_a += value
        else:
            score_b += value
    print(score_a - score_b)


if __name__ == '__main__':
    my_answer()
