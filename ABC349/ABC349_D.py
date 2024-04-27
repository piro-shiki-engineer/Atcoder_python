def my_answer():
    L, R = map(int, input())


def is_airport_code(s, t):
    n = len(s)
    t = t.upper()

    for i in range(n):
        if s[i].upper() == t[0]:
            for j in range(i + 1, n):
                if s[j].upper() == t[1]:
                    for k in range(j + 1, n):
                        if s[k].upper() == t[2]:
                            return "Yes"
    if t[2] == 'X':
        for i in range(n):
            if s[i].upper() == t[0]:
                for j in range(i + 1, n):
                    if s[j].upper() == t[1]:
                        return "Yes"

    return "No"


if __name__ == '__main__':
    # Input example
    s = input()
    t = input()

    # Function call
    result = is_airport_code(s, t)
    print(result)