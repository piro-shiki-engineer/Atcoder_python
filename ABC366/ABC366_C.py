from collections import defaultdict


def main():
    Q = int(input())
    sack = defaultdict(int)
    for _ in range(Q):
        query_i = list(map(int, input().split()))
        if query_i[0] == 1:
            sack[query_i[1]] += 1
        elif query_i[0] == 2:
            sack[query_i[1]] -= 1
            if sack[query_i[1]] == 0:
                del sack[query_i[1]]
        elif query_i[0] == 3:
            print(len(sack.keys()))


if __name__ == '__main__':
    main()
