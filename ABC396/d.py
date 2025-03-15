def main():
    N = int((input()))
    a_ = list(map(int, input().split()))

    for i in range(N-2):
        print(i, a_[i], a_[i+1], a_[i+2])
        if a_[i] == a_[i+1] == a_[i+2]:
            print("Yes")
            exit()
    print("No")


if __name__ == '__main__':
    main()