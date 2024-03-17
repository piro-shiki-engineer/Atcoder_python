def my_answer():
    S = input()
    flag_bigger = False
    flag_smaller = False
    other = True
    if S[0] == "<":
        flag_smaller = True
    if S[-1] == ">":
        flag_bigger = True

    for i in range(1, len(S)-1):
        if not S[i] == "=":
            other = False

    if flag_smaller and flag_bigger and other:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    my_answer()
