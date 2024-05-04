def my_answer():
    A_final = sum(list(map(int, input().split())))
    B_eight = sum(list(map(int, input().split())))

    print(A_final - B_eight + 1)


if __name__ == '__main__':
    my_answer()