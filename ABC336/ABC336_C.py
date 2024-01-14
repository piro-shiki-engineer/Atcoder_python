
def judge_all_even(x: int) -> bool:
    string = str(x)

    for word in string:
        if int(word) % 2 != 0:
            return False
    return True


def my_answer():
    n = int(input())
    n = n - 1
    answer = ''

    if n == 0:
        print(0)
        exit()

    while n > 0:
        answer += str(n % 5)
        n = n // 5

    print(int(answer[::-1])*2)


if __name__ == '__main__':
    my_answer()
