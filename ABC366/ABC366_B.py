def main():
    N = int(input())
    chars_list = [input() for _ in range(N)]
    max_length = max(len(s) for s in chars_list)

    for i in range(N):
        if len(chars_list[i]) < max_length:
            chars_list[i] += "*" * (max_length - len(chars_list[i]))

    for i in range(max_length):
        T_i = ""
        for j in range(N):
            T_i += chars_list[j][i]
        T_i = T_i.rstrip('*')
        print(T_i)


if __name__ == '__main__':
    main()
