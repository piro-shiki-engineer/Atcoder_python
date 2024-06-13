def sierpinski_carpet(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]

    if n == 0:
        memo[n] = '#'
        return memo[n]

    prev_carpet = sierpinski_carpet(n-1, memo)
    size = len(prev_carpet)
    carpet = []

    for y in range(3*size):
        row = ''
        for x in range(3*size):
            if size <= x < size*2 and size <= y < size*2:
                row += '.'
            else:
                row += prev_carpet[y % size][x % size]
        carpet.append(row)

    return carpet


def my_answer():
    level = int(input())
    carpet = sierpinski_carpet(level)

    for row in carpet:
        print(row)


if __name__ == '__main__':
    my_answer()
