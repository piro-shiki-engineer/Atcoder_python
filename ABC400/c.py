def main():
    N = int(input())
    res = 0
    good_nums = set()

    a = 1
    while 2**a <= N:
        power = 2**a

        b = 1
        while power * (b**2) <= N:
            X = power * (b**2)
            good_nums.add(X)
            b += 1

        a += 1

    print(len(good_nums))


if __name__ == "__main__":
    main()
