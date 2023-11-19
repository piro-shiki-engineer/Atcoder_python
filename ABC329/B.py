def my_answer():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    a.sort(reverse=True)
    max_value = a[0]

    for i in range(n):
        if a[i] != max_value:
            b.append(a[i])
    b.sort(reverse=True)
    next_max = b[0]

    print(next_max)


if __name__ == '__main__':
    my_answer()
