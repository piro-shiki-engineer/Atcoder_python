def my_answer():
    S = input()
    pattern_list = []

    for i in range(len(S)+1):
        S_from_i = S[i:]
        j = len(S)
        if len(S_from_i) > 1:
            S_from_i_to_j = S_from_i
            while len(S_from_i_to_j) > 1:
                S_from_i_to_j = S_from_i[:j]
                pattern_list.append(S_from_i_to_j)
                j -= 1
        elif len(S_from_i) == 1:
            pattern_list.append(S_from_i)
    pattern_list = list(set(pattern_list))
    print(len(pattern_list))


if __name__ == '__main__':
    my_answer()
