
def my_answer():
    A, M, L, R = map(int, input().split())

    count = 0
    x_p = A
    x_m = A
    next_R = False
    next_L = False



    if L != R:
        next_R = True
        next_L = True
    else:
        print("L = R")
        print(count)

    while True:

        x_p += M
        x_m -= M
        print(x_p, x_m)

        if x_p < R:
            count += 1
        elif x_p == R:
            count += 1
            next_R = True
        else:
            next_R = False

        if L < x_m:
            count += 1
        elif L == x_m:
            count += 1
            next_L = False
        else:
            next_L = False

        if next_R and next_L:
            break


    print(x_p, x_m)
    print('木の数',count)

def my_answer2():
    A, M, L, R = map(int, input().split())

    # Lの方向の最初のツリーの位置
    first_tree_L = A + ((L - A + M - 1) // M) * M
    # Rの方向の最後のツリーの位置
    last_tree_R = A + ((R - A) // M) * M

    # この範囲内にあるツリーの総数を計算
    if first_tree_L <= last_tree_R:
        total_trees = ((last_tree_R - first_tree_L) // M) + 1
    else:
        total_trees = 0

    print(total_trees)


if __name__ == '__main__':
    my_answer2()
