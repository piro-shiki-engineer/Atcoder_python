def main():
    N = int((input()))
    a_list = list(map(int, input().split()))

    for i in range(N-1):
        if not a_list[i] < a_list[i+1]:
            print("No")
            exit()
    print("Yes")


if __name__ == '__main__':
    main()