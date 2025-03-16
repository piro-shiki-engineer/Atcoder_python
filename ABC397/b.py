def main():
    s = input()
    res = 0
    position = 0

    for char in s:
        expected = "i" if position == 0 else "o"

        if char == expected:
            position = 1 - position
        else:
            res += 1

    if (len(s) + res) % 2 == 1:
        res += 1

    print(res)


if __name__ == "__main__":
    main()
