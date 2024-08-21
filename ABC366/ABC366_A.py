def main():
    N, T, A = map(int, input().split())
    if abs(T-A) > N-(T+A):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()