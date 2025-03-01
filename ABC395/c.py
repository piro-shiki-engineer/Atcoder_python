def main():
    N = int(input())
    a_list = list(map(int, input().split()))

    min_length = float("inf")
    left = 0
    seen = {}

    for right in range(N):
        if a_list[right] in seen and seen[a_list[right]] >= left:
            length = right - seen[a_list[right]] + 1
            min_length = min(min_length, length)

        seen[a_list[right]] = right

    print(min_length if min_length != float("inf") else -1)


if __name__ == "__main__":
    main()
