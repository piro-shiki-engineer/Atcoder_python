def my_answer():
    n, total = map(int, input().split())
    x, y, z = -1, -1, -1

    for i in range(n+1):
        for j in range(n+1-i):
            for k in range(n+1-i-j):
                count = 10000*i + 5000*j + 1000*k
                if count == total:
                    x = i
                    y = j
                    z = k
                    break
    print("{} {} {}".format(x, y, z))



if __name__ == '__main__':
    my_answer()
