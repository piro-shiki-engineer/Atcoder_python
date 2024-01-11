
def my_answer():
    N = int(input())

    num_conb = []

    for x in range(N+1):
        for y in range(N+1):
            for z in range(N+1):
                if x+y+z <= N:
                    num_conb.append([x, y, z])
                    print(str(x) + str(' ') + str(y) + str(' ') + str(z))


if __name__ == '__main__':
    my_answer()
