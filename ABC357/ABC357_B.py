def my_answer():
    S = input()
    lower = 0
    upper = 0

    for i in range(len(S)):
        s_i = S[i]

        if ord(s_i) - ord("A") < 32:
            upper += 1
        else:
            lower += 1

    if lower > upper:
        print(S.lower())
    else:
        print(S.upper())


if __name__ == "__main__":
    my_answer()
