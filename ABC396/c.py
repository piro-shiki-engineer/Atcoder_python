def main():
    """
    _, 0, 1, 2, 3,
    number_of_black_ball > number_of_white_ball
    白0、黒1以上になる
    """
    n, m = map(int, input().split())
    black_balls = list(map(int, input().split()))
    white_balls = list(map(int, input().split()))

    black_balls.sort(reverse=True)
    white_balls.sort(reverse=True)

    max_val = 0
    for i in range(n+1):
        for j in range(m+1):
            if i >= j:
                max_val = max(max_val, sum(black_balls[:i])+sum(white_balls[:j]))

    print(max_val)


if __name__ == '__main__':
    main()