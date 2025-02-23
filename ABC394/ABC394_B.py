def main():
    N = int(input())
    s_list = []

    for _ in range(N):
        s_list.append(input())

    sorted_s_list = sorted(s_list, key = lambda x: len(x))
    print("".join(sorted_s_list))

if __name__ == '__main__':
    main()
