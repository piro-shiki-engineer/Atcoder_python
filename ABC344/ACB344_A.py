def my_answer():
    S = list(input())
    flag = True
    ans = []
    for string in S:
        if string == '|':
            if flag:
                flag = False
            else:
                flag = True
            continue
        elif flag:
            ans.append(string)
    print(''.join(ans))


if __name__ == '__main__':
    my_answer()
