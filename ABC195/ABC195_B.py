def my_answer():
    A, B, W = map(int, input().split())
    W = W*1000
    min_val = 10**14
    max_val = -10**14

    for x in range(1, 10**6+1):
        if A*x <= W <= B*x:
            min_val = min(x, min_val)
            max_val = max(x, max_val)

    if min_val == 10**14:
        print("UNSATISFIABLE")
        exit()

    print("{} {}".format(min_val, max_val))


if __name__ == '__main__':
    my_answer()
