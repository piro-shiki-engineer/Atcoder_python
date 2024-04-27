def my_answer():
    S = input()
    alphabet_count = {chr(ord('a') + i): 0 for i in range(26)}

    for i in range(len(S)):
        s_i = S[i]
        alphabet_count[s_i] += 1

    i = 1
    while i <= max(alphabet_count.values()):
        count = 0
        for value in alphabet_count.values():
            if value == i:
                count += 1
        if count == 0 or count == 2:
            pass
        else:
            print("No")
            exit()
        i += 1

    print("Yes")


if __name__ == '__main__':
    my_answer()
