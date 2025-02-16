def main():
    N, M = map(int, input().split())
    exist_big_brother = [False]*(N+1)

    for _ in range(M):
        A, B = map(str, input().split())
        A = int(A)
        if not exist_big_brother[A] and B == "M":
            exist_big_brother[A] = True
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
