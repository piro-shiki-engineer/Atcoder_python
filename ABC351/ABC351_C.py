from collections import deque

def my_answer():
    N = int(input())
    A_list = list(map(int, input().split()))
    line = deque()

    for i in range(N):
        line.append(A_list[i])

        # ポイントは短絡評価
        while len(line) >= 2 and line[-1] == line[-2]:
            right_1 = line[-1]
            right_2 = line[-2]

            if right_1 != right_2:
                pass
            else:
                if right_1 == 0 and right_2 == 0:
                    replace_ball = 1
                else:
                    replace_ball = right_1 + 1
                line.pop()
                line.pop()

                line.append(replace_ball)
    print(len(line))


if __name__ == '__main__':
    my_answer()