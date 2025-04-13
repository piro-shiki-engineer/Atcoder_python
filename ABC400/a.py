def main():
    A = int(input())
    B = 400 // A if 400 % A == 0 else -1
    print(B)


if __name__ == '__main__':
    main()
