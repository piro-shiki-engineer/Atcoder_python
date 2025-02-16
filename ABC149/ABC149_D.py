from collections import deque


def my_answer():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    hands = []
    ans = 0

    for i in range(N):
        if T[i] == "r":
            if i < K:
                ans += P
                hands.append("p")
            elif K <= i and hands[i - K] != "p":
                ans += P
                hands.append("p")
            else:
                hands.append("x")

        if T[i] == "s":
            if i < K:
                ans += R
                hands.append("r")
            elif K <= i and hands[i - K] != "r":
                ans += R
                hands.append("r")
            else:
                hands.append("x")

        if T[i] == "p":
            if i < K:
                ans += S
                hands.append("s")
            elif K <= i and hands[i - K] != "s":
                ans += S
                hands.append("s")
            else:
                hands.append("x")
    print(ans)


if __name__ == '__main__':
    my_answer()
