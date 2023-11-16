
def my_answer():
    N = int(input())
    d = [0]*N
    for i in range(N):
        d[i] = int(input())

    d.sort(reverse=True)
    count = 1
    tmp = d[0]

    for i in range(1, N):
        if d[i] < tmp:
            count += 1
            tmp = d[i]
        else:
            tmp = d[i]
            continue

    print(count)


if __name__ == '__main__':
    my_answer()
