from collections import deque


def my_answer():
    S = list(input())
    Q = int(input())
    query_list = [list(input().split()) for _ in range(Q)]
    ans = deque()
    inv = False

    for i in range(len(S)):
        ans.append(S[i])

    for query in query_list:
        if query[0] == '1':
            if inv:
                inv = False
            else:
                inv = True
        else:
            F, C = query[1], query[2]
            if inv:
                if F == '1':
                    ans.append(C)
                    pass
                elif F == '2':
                    ans.appendleft(C)
            else:
                if F == '1':
                    ans.appendleft(C)
                    pass
                elif F == '2':
                    ans.append(C)
    ans = ''.join(ans)
    if inv:
       print(ans[::-1])
    else:
        print(ans)


if __name__ == '__main__':
    my_answer()
