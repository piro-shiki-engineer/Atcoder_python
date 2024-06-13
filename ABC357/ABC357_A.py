def my_answer():
    N, M = map(int, input().split())
    nums_of_hands = list(map(int, input().split()))
    can_sanitize = 0

    for i in range(N):
        M -= nums_of_hands[i]
        if M >= 0:
            can_sanitize += 1
    print(can_sanitize)


if __name__ == "__main__":
    my_answer()
