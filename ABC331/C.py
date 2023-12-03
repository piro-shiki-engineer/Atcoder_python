from collections import defaultdict


def my_answer():
    N = int(input())
    A = list(map(int, input().split()))
    B = defaultdict(list)
    ans = [0]*N
    total = 0

    for index, value in enumerate(A):
        B[value].append(index)
    # print(B)
    # print(sorted(B.items()))
    for val, i_list in sorted(B.items(), reverse=True):
        # print(val, i_list)
        for i in i_list:
            ans[i] = total
        total += val

    print(*ans)



if __name__ == '__main__':
    my_answer()
