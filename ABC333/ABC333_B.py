
def my_answer():
    S = list(input())
    S = sorted(S)
    T = list(input())
    T = sorted(T)
    s1, s2 = S[0], S[1]
    t1, t2 = T[0], T[1]

    print(S, T)

    P = ['A', 'B', 'C', 'D', 'E']
    index_s1 = P.index(s1)
    index_s2 = P.index(s2)
    index_t1 = P.index(t1)
    index_t2 = P.index(t2)


    if (index_s2 - index_s1) == 1:
        s_length = 1
    else:
        s_length = 2

    if (index_t2 - index_t1) == 1:
        t_length = 1
    else:
        t_length = 2

    if s_length == t_length:
        print("Yes")
    else:
        print("No")

    print(S)
    print(T)

if __name__ == '__main__':
    my_answer()