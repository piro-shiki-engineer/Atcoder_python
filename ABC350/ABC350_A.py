def my_answer():
    S = input()
    contest = []

    if "ABC" != S[:3]:
        print("No")
        exit()

    for i in range(1, 350):
        if i < 100:
            if i < 10:
                contest.append("ABC00" + str(i))
            else:
                contest.append("ABC0" + str(i))
        else:
            if i == 316:
                continue
            else:
                contest.append("ABC" + str(i))

    if S in contest:
        print("Yes")
    else:
        print("No")




if __name__ == '__main__':
    my_answer()