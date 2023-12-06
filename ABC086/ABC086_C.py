

def my_answer():
    n = int(input())
    plan = []
    plan_judge = True
    for i in range(n):
        plan.append(list(map(int, input().split())))

    t = 0
    x = 0
    y = 0

    for t_i, x_i, y_i in plan:
        diff_t = t_i - t
        diff_x = abs(x_i - x)
        diff_y = abs(y_i - y)
        diff_total = diff_x + diff_y

        if diff_total > diff_t:
            plan_judge = False
            break
        #時間差と座標差の偶奇は同じである必要がある
        if diff_t % 2 != diff_total % 2:
            plan_judge = False
            break

        t = t_i
        x = x_i
        y = y_i

    if plan_judge:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    my_answer()
