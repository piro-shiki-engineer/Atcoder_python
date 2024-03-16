def my_answer():
    X = int(input())
    for A in range(-10**3, 10**3):
        for B in range(-10**3, 10**3):

            if (A**5-B**5) == X:
                print("{} {}".format(A, B))
                exit()


if __name__ == '__main__':
    my_answer()
