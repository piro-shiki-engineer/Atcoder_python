def my_answer():
    N = int(input())
    ans = []
    for i in range(1, N+1):
        val = i
        if N % val == 0:
            ans.append(val)
            ans.append(N//val)
        if val**2 > N:
            break
    ans.sort()

    for i in range(len(ans)):
        print(ans[i])


if __name__ == '__main__':
    my_answer()
