def my_answer():
    S, T = map(str, input().split())
    for w in range(1, len(S)):
        for c in range(1, w+1):
            created_s = ''
            i = c - 1
            while i < len(S):
                if i < len(S):
                    created_s += S[i]
                i += w
            if created_s == T:
                print('Yes')
                exit()
    print('No')


if __name__ == '__main__':
    my_answer()
