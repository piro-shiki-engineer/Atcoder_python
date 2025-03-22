def main():
    cards = list(map(int, input().split()))

    count_unique_val = {}
    for card in cards:
        count_unique_val[card] = count_unique_val.get(card, 0) + 1

    counts = sorted(count_unique_val.values(), reverse=True)

    if len(counts) >= 2 and counts[0] >= 3 and counts[1] >= 2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
