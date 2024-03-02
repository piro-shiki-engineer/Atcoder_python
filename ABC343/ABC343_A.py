def my_answer():
    A, B = map(int, input().split())
    sum = A + B
    ans = int(sum / 2)

    if ans == 0:
        print(9)
    else:
        print(ans)


if __name__ == '__main__':
    my_answer()
