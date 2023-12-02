def my_answer():
    M, D = map(int, input().split())
    y, m, d = map(int, input().split())

    next_month = False
    next_year = False

    d += 1
    if d > D:
        next_month = True
        d = 1

    if next_month:
        m += 1

    if m > M:
        next_year = True
        m = 1

    if next_year:
        y += 1

    print('{} {} {}'.format(y, m, d))


if __name__ == '__main__':
    my_answer()
