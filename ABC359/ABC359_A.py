def my_answer():
    N = int(input())
    t = 0

    for _ in range(N):
        s = input()
        if s == 'Takahashi':
            t += 1
    print(t)


if __name__ == '__main__':
    my_answer()
