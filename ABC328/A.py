N, X = map(int, input().split())
S = list(map(int, input().split()))

total = 0
for i in range(N):
    if S[i] <= X:
        total += S[i]

print(total)
