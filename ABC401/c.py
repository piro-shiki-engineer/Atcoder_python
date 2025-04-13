def main():
    n, k = map(int, input().split())
    mod = 10 ** 9
    a_list = []

    total_window = 0
    i = 0
    while i < k:
        a_list.append(1)
        total_window += 1
        i += 1

    while i < n + 1:
        a_list.append(total_window)
        total_window = (total_window + a_list[i] - a_list[i - k])

        i += 1

    print(a_list[n] % mod)


if __name__ == "__main__":
    main()
