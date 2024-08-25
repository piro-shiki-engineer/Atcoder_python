from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    while True:
        A.sort(reverse=True)
        positive_count = 0
        for a_i in A:
            if a_i > 0:
                positive_count += 1
        if positive_count <= 1:
            break

        A[0] -= 1
        A[1] -= 1
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
