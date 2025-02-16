import itertools

def my_answer():
    N = int(input())
    A_list = list(map(int, input().split()))

    ans = 0

    for l in range(N):
        A_min_num = A_list[l]
        for r in range(l,N):
            A_min_num = min(A_min_num, A_list[r])
            ans = max(ans, r-l+1)
    print(ans)


if __name__ == '__main__':
    my_answer()
