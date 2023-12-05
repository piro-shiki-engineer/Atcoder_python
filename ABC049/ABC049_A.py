

def my_answer():
    s = input()
    t = str()
    judge = True

    words = ['dream', 'dreamer', 'erase', 'eraser']

    while judge:
        for word in words:
            if word == s[-(len(word)):]:
                t += word
                s = s[: (len(s)-(len(word)))]
                if len(s) == 0:
                    print('YES')
                    judge = False
                break

            elif word == words[-1]:
                print('NO')
                judge = False
                break


if __name__ == '__main__':
    my_answer()
