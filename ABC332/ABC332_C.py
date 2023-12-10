
def my_answer():
    N, M = map(int, input().split())
    S = list(input())

    plain = M
    logo = 0
    logo_needed = 0

    for i in range(N):
        if S[i] == "1":
            if plain > 0:
                plain -= 1
            elif logo > 0:
                logo -= 1
            else:
                logo_needed += 1
        elif S[i] == "2":
            if logo > 0:
                logo -= 1
            else:
                logo_needed += 1
        elif S[i] == "0":
            plain = M
            logo = logo_needed

    print(logo_needed)


if __name__ == '__main__':
    my_answer()
