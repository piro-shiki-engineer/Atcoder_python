
def my_answer():
    N, X = map(int, input().split())
    S = list(map(int, input().split()))

    total = 0
    for i in range(N):
        if S[i] <= X:
            total += S[i]

    print(total)

if __name__ == '__main__':
    my_answer()
