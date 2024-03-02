def my_answer():
    N = int(input())
    i = 1
    K = i**3
    ans = 0
    flag = False
    possible = False

    while K <= N:
        K_possible = str(K)

        if len(K_possible) == 1:
            possible = True

        elif len(K_possible) >= 2:
            for j in range(int(len(K_possible)/2)):
                val_j = K_possible[j]
                val_j_reverse = K_possible[-(j+1)]

                if val_j != val_j_reverse:
                    possible = False
                    break
                elif val_j == val_j_reverse:
                    possible = True

        if possible == True:
            ans = max(ans, K)

        i += 1
        K = i**3
        flag = False
        possible = False
    print(ans)


if __name__ == '__main__':
    my_answer()
