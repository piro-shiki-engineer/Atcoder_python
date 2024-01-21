def my_answer():
    S = input()
    str_A = ''
    str_B = ''
    str_C = ''
    str_ABC = ''

    for i in range(len(S)):
        s_i = S[i]
        if s_i == 'A':
            str_A += s_i
        elif s_i == 'B':
            str_B += s_i
        elif s_i == 'C':
            str_C += s_i
    str_abc = str_A + str_B + str_C
    if S == str_abc:
        print("Yes")
    elif S != str_abc:
        print("No")




if __name__ == "__main__":
    my_answer()
