def my_answer():
    n = int(input())
    s = list(map(str, input()))
    s_part = []
    tmp = str
    for i in range(n):
        if s[i] not in s_part:
            s_part.append(s[i])
        elif tmp not in s_part:
            tmp = str(tmp) + s[i]
            s_part.append(tmp)
        else:
            tmp = str

    print(len(s_part))


if __name__ == '__main__':
    my_answer()
