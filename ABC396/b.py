def main():
    Q = int(input())
    cards = [0 for _ in range(100)]
    for _ in range(Q):
        query = input()
        opt = query.split()[0]

        if opt == "1":
            _, x = query.split()
            cards.append(int(x))

        else:
            print(cards.pop())



if __name__ == '__main__':
    main()